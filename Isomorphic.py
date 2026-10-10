def are_isomorphic(s, t):
    map_s_t={}
    map_t_s={}

    for c1,c2 in zip(s,t):
        if c1 in map_s_t and map_s_t[c1]!=c2:
            return False
        
        if c2 in map_t_s and map_t_s[c2]!=c1:
            return False
        
        map_s_t[c1]=c2
        map_t_s[c2]=c1
    return True



if __name__ == "__main__":
    s=input("s: ").strip()
    t=input("t: ").strip()
    print(are_isomorphic(s,t))