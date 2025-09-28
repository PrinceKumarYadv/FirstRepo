import pywhatkit  # pyright: ignore[reportMissingImports]
import datetime
import time

def send_instant_message():
    number = input("Enter Phone Number with Country Code (e.g. Phone Number): ")
    message = input("Enter your message: ")
    print(f"Sending message instantly to {number}...")
    pywhatkit.sendwhatmsg_instantly(number, message, wait_time=10, tab_close=True)
    print(" Message sent successfully!\n")


def send_scheduled_message():
    number = input("Enter Phone Number with Country Code (e.g. Phone number): ")
    message = input("Enter your message: ")
    print("\nEnter the time to send message (24-hour format)")
    hour = int(input("Hour (0-23): "))
    minute = int(input("Minute (0-59): "))

    today = datetime.date.today()
    send_time = datetime.datetime(today.year, today.month, today.day, hour, minute)

    if send_time <= datetime.datetime.now():
        send_time += datetime.timedelta(days=1)

    print(f" Scheduled message to {number} at {send_time.strftime('%Y-%m-%d %H:%M')}")
    pywhatkit.sendwhatmsg(number, message, send_time.hour, send_time.minute)
    print(" Message scheduled successfully!\n")


def send_multiple_messages():
    number = input("Enter Phone Number with Country Code (e.g. +919876543210): ")
    count = int(input("How many messages do you want to send? "))
    message = input("Enter your message: ")

    print(f" Sending {count} messages to {number}...")
    for i in range(count):
        pywhatkit.sendwhatmsg_instantly(number, f"{message} ({i+1})", wait_time=8, tab_close=True)
        time.sleep(5)  # short delay between messages
    print(" All messages sent successfully!\n")


def main():
    while True:
        print("\n WhatsApp Automation Project")
        print("1. Send Instant Message")
        print("2. Schedule Message")
        print("3. Send Multiple Messages")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            send_instant_message()
        elif choice == "2":
            send_scheduled_message()
        elif choice == "3":
            send_multiple_messages()
        elif choice == "4":
            print(" Exiting... Goodbye!")
            break
        else:
            print(" Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()      
       
         
         
