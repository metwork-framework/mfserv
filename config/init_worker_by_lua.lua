local stats = require('stats')
local admin_hostname = os.getenv('MFSERV_ADMIN_HOSTNAME')
local telegraf_statsd_port = tonumber(os.getenv('MFSERV_TELEGRAF_STATSD_PORT'))
local new_timer = ngx.timer.at
local delay = 0.1
local cjson = require "cjson"
local upstream = require "ngx.upstream"

local function string_starts(String, Start)
    return string.sub(String,1,string.len(Start))==Start
end

local function process()
    if admin_hostname ~= "null" then
        stats.init({host="127.0.0.1", port=telegraf_statsd_port, delay=500})
    end
    local check
    check = function(premature)
        if not premature then
            local peers = ngx.shared.peers
            local keys = peers:get_keys()
            for _, key in ipairs(keys) do
                if string_starts(key, "peers") then
                    local value = peers:get(key)
                    if value ~= nil then
                        local dvalue = cjson.decode(value)
                        if dvalue ~= nil then
                            upstream.set_peer_down(dvalue['name'], false, dvalue['id'], dvalue['down'])
                        end
                    end
                end
            end
            local ok, err = new_timer(delay, check)
            if not ok then
                ngx.log(ngx.ERR, "failed to create timer: ", err)
                return
            end
        end
     end
     local hdl, err = new_timer(delay, check)
     if not hdl then
         ngx.log(ngx.ERR, "failed to create timer: ", err)
         return
     end
end

return process
