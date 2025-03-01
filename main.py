from send_texts import send_texts
from emails import pull_emails

def main():
    pull_emails()
    send_texts()

if __name__=="__main__":
    main()