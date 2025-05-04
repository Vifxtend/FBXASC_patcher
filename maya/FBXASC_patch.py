import maya.cmds as cmd


FBX_SPECIAL = {
                'FBXASC033': '!',
                'FBXASC064': '@',
                'FBXASC035': '#',
                'FBXASC036': '$',
                'FBXASC037': '%',
                'FBXASC094': '^',
                'FBXASC092': '\\',
                'FBXASC038': '&',
                'FBXASC042': '*',
                'FBXASC040': '(',
                'FBXASC041': ')',
                'FBXASC046': '.',
                'FBXASC047': '/',
                'FBXASC044': ',',
                'FBXASC124': '|',
                'FBXASC034': '"',
                'FBXASC058': ':',
                'FBXASC059': ';',
                'FBXASC093': ']',
                'FBXASC091': '[',
                'FBXASC043': '+',
                'FBXASC061': '=',
                'FBXASC045': '-',
                'FBXASC060': '<',
                'FBXASC062': '>',
                'FBXASC032': 'spacebar'
               }


#function to catch all bad codes and return in array
def get_bad(string=str):
    bad_array = []
    
    for bad_code, symbol in FBX_SPECIAL.items():
        if bad_code in string:
            bad_array.append(bad_code)
            
    return bad_array


#entry point
def run_batch_rename():

    cmd.undoInfo(ock=1)

    for node in cmd.ls(ni=1):
        bad_size = len(get_bad(node))

        if bad_size > 0:
            good_name = ''
            bad_codes = get_bad(node)

            for i in range(bad_size):
                good_name = node.replace(bad_codes[i], '_')

            try:
                cmd.rename(node, good_name)

            except: pass

    cmd.undoInfo(cck=1)


    
run_batch_rename()