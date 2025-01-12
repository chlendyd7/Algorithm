import re
def solution(new_id:str):
    new_id = new_id.lower()
    new_id = re.sub(r"[^a-z0-9._-]", "", new_id)
    new_id = re.sub(r"\.+", ".", new_id)
    new_id = new_id.strip('.')
    
    if not new_id: new_id = 'a'
    
    if len(new_id) > 15:
        new_id = new_id[:15].rstrip('.')
    
    while len(new_id) < 3:
        new_id += new_id[-1]
    
        
    return new_id