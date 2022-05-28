from p3 import msg_to_binary
from p2 import dec_to_bin
from p6 import Hs,exp,g,p

n =64
def merkle_hash(msg, iv):
    msg = msg_to_binary(msg)
    l = len(msg)
    msg_len = dec_to_bin(l).zfill(n)
    result = iv.zfill(n)
    for i in range(0,l,n):
        cur_msg=msg[i:i+n]
        if n != len(cur_msg):
            cur_msg = cur_msg.ljust(n,"0")
        result=Hs(cur_msg, result)
    
    result = Hs(msg_len,result)
    return result

def main():
    text ="test string for merkle hash"
    final_str = merkle_hash(text,"1011110101010101101011")
    print("Text:",text)
    print("enc string: ",final_str)
    print("Length:" +str(len(final_str)))

if __name__ == '__main__':
    main()
