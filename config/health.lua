local status_file = os.getenv("MODULE_RUNTIME_HOME") .. "/var/status"

local function load_status()
    local f = io.open(status_file, "r")
    if f == nil then
        return "NOT FOUND"
    end
    local content = f:read()
    f:close()
    return content
end

local function process()
    local status = load_status()
    if status == "RUNNING" then
        ngx.status = 200
        ngx.say("OK")
    else
        ngx.status = 503
        if status == "STARTING" then
            ngx.say("STARTING")
        elseif status == "STOPPING" then
            ngx.say("STOPPING")
        elseif status == "ERROR" then
            ngx.say("ERROR")
        else
            ngx.say("UNKNOWN")
        end
    end
end

return process
