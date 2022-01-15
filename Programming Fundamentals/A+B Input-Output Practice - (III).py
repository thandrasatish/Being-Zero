def main():
    while True:
        try:
            a,b=map(int,input().split())
            if(a==0 and b==0):
                pass
            else:
                print(a+b)
        except EOFError:
            break
if __name__ == "__main__":
	main()
