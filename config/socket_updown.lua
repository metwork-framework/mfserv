local cjson = require "cjson"
local upstream = require "ngx.upstream"
local get_upstreams = upstream.get_upstreams
local b64 = require("ngx.base64")

local function _set(upstream_name, peer_id, down)
    local peers = ngx.shared.peers
    local t = {}
    t["name"] = upstream_name
    t["id"] = tonumber(peer_id)
    t["down"] = down
    local key = "peers_" .. t["name"] .. "_" .. peer_id
    peers:set(key, cjson.encode(t), 2)
end

local function get_conns(socket_path)
    local conns = 0
    local us = get_upstreams()
    local u, v
    for _, u  in ipairs(us) do
        local ppeers = upstream.get_primary_peers(u)
        for _, v in ipairs(ppeers) do
            if v['name'] == "unix:" .. socket_path then
                conns = conns + v['conns']
            elseif v['name'] == socket_path then
                conns = conns + v['conns']
            end
        end
    end
    return conns
end

local function process(b64_socket, down)
    local wait = false
    if down and ngx.var.arg_wait == '1' then
        wait = true
    end
    local decoded, err = b64.decode_base64url(b64_socket)
    if decoded == nil then
        ngx.log(ngx.ERR, "failed to decode base64 value: ", err)
        return
    end
    local found = false
    local us = get_upstreams()
    local u, v
    for _, u  in ipairs(us) do
        local ppeers = upstream.get_primary_peers(u)
        for _, v in ipairs(ppeers) do
            if v['name'] == "unix:" .. decoded then
                _set(u, v['id'], down)
                found = true
            elseif v['name'] == decoded then
                _set(u, v['id'], down)
                found = true
            end
        end
    end
    if not found then
        ngx.log(ngx.DEBUG, "can't find ", decoded)
    end
    if wait then
        while true do
            local conns = get_conns(decoded)
            if conns == 0 then
                break
            end
            ngx.sleep(0.5)
        end
    end
end

return process
