import fb

def main():
    user,pwd=fb.get_login()
    fb.facebook_group_post(user,pwd)


if __name__=="__main__":
    main()
