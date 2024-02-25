'''def demo(*sports):
    print("the list of game played:")
    for name in sports:
        print(name)
demo('cricket',"vollyball","chess", "hockey", "PUBG")'''
def demo(*name):
     print("the list of game played",name)
     print("name=",name[0])
     print("name=",name[1])
     print("name=",name[2])
demo('cricket',"vollyball","chess", "hockey", "PUBG")
