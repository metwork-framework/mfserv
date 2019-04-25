local upstream = require "ngx.upstream"
local get_upstreams = upstream.get_upstreams
local cjson = require "cjson"

local function process()
    local res = {}
	local us = get_upstreams()
	for _, u in ipairs(us) do
        local peers = upstream.get_primary_peers(u)
        res[u] = peers
	end
    ngx.print(cjson.encode(res))
end

return process
