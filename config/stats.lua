local _M = {}

local statsd = require("resty.statsd")
local mfutil = require("mfutil")
local _statsd_instance = nil
local _statsd_options = nil

function _M.init(statsd_options)

    _statsd_options = statsd_options

end

local function get_statsd_instance()
    if _statsd_instance == nil then
        if _statsd_options == nil then
            mfutil.exit_with_ngx_error(500, "stats module not initiliazed", "SAME")
        end
        _statsd_instance = statsd.new(_statsd_options)
    end
    return _statsd_instance
end

local function get_tags(plugin, app, typ)

    local tags = { plugin=plugin, app=app }
    tags["type"] = typ
    local status = tonumber(ngx.var.status)
    if status == nil then
        tags["status_code"] = "unknown"
    else
        tags["status_code"] = tostring(status)
    end
    return tags

end

function _M.send_status_code_stat(measurement, plugin, app, typ)

    local tags = get_tags(plugin, app, typ)
    statsd.count(get_statsd_instance(), measurement, 1, 1, tags)

end

function _M.send_timing_stat(measurement, plugin, app, typ)

    if ngx.var.request_time == nil then
        return
    end
    local tags = get_tags(plugin, app, typ)
    local time_ms = math.floor(1000.0 * ngx.var.request_time)
    statsd.timing(get_statsd_instance(), measurement, time_ms, tags)

end

return _M
