from jinja2_shell_extension import shell
from jinja2_getenv_extension import getenv
from jinja2_fnmatch_extension import _fnmatch
from jinja2_from_json_extension import from_json


def define_env(env):

    # ***** Variables *****
    env.variables['components'] = "../850-reference/100-components"
    env.variables['config_ini'] = "../850-reference/200-config_ini"
    env.variables['installation_guide'] = "../100-installation_guide"
    env.variables['addons'] = "../840-addons"

    # ***** Filters *****
    env.filters["shell"] = shell
    env.filters["getenv"] = getenv
    env.filters["fnmatch"] = _fnmatch
    env.filters["from_json"] = from_json

    # ***** Macros *****

    @env.macro
    def declare_utility(name, cmd=None, level=3, custom_anchor=None,
                        layers="default@mfext"):
        res = []
        anchor = ""
        if custom_anchor != "AUTO":
            anchor = "{: #%s}" % \
                (custom_anchor if custom_anchor is not None else name)
        _cmd = cmd
        if _cmd is None:
            _cmd = "%s --help" % name
        _cmd2 = "layer_wrapper --layers=%s -- %s" % (layers, _cmd)
        res.append("%s %s %s" % ('#' * level, name, anchor))
        res.append("")
        res.append("```console")
        res.append("$ %s" % _cmd)
        res.append(shell(None, _cmd2))
        res.append("```")
        res.append("")
        return "\n".join(res)

    @env.macro
    def link_utility(name, number=750, page="utilities"):
        return "[`%s`](../%i-%s#%s)" % (name, number, page, name)
