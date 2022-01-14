import subprocess

def res_cmd_lfeed(cmd):
    return subprocess.Popen(
            cmd,stdout=subprocess.PIPE,
            shell=True).stdout.readlines()

def main():
    text =str(input("Please register car number: "))
    cmd = ("alpr -n 5 ea7the.jpg")
    data=res_cmd_lfeed(cmd)
    result=[]
    for i in range(1,len(data)):
        if ( text in (data[i].decode())):
            result+=["True"]
        else:
            result+=["False"]
    if "True" in result:
        print("あなたの車です。")
    else:
        print("違法駐車の可能性大!!!")
if __name__=='__main__':
    main()
