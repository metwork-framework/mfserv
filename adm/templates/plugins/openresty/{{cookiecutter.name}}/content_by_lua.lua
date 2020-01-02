local function process()
    ngx.status = 200
    ngx.say("Hello World, this is request_id: " .. ngx.var.request_id)
end

return process
