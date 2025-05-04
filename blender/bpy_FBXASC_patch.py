import bpy


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
               


def get_fbxasc(string=str):
    bad_array = []
    
    for bad_code, symbol in FBX_SPECIAL.items():
        if bad_code in string:
            bad_array.append(bad_code)
            
    return bad_array



def fbxasc_patch(name:str):
    
    bad_size = len(get_fbxasc(name))
        
    if bad_size > 0:
        good_name = ''
            
        bad_codes = get_fbxasc(name)
        obj_name = name
            
        for i in range(bad_size):
                
            good_name = obj_name.replace(bad_codes[i], '_')
            obj_name = good_name
            
            
        return obj_name
            

    
#entry point
def run_batch_rename():
    
    #patch object names:
    for obj in bpy.data.objects:
        
        try:
            obj.name = fbxasc_patch(obj.name)
            
        except: pass
    

    #patch bone names:
    skeletons = list()
    
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            skeletons.append(obj.name)
            
    
    for skeleton in skeletons:
        for bone in bpy.data.objects[skeleton].pose.bones:
            
            try:
                bone.name = fbxasc_patch(bone.name)
                
            except: pass


    #patch armaure data blocks:
    for skel in bpy.data.armatures:
        try:
            skel.name = fbxasc_patch(skel.name)

        except: pass


    #patch material names:
    for mat in bpy.data.materials:
        
        try:
            mat.name = fbxasc_patch(mat.name)

        except: pass



    #patch mesh data blocks:
    for mesh in bpy.data.meshes:
        try:
            mesh.name = fbxasc_patch(mesh.name)

        except: pass


        
run_batch_rename()