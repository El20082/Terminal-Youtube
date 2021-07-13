
# Import library of functions we will use for filewriting .etc
import lib.backend

# Global variables to use to store current channel information
channel_name = ""
channel_number_of_subscribers = 0
channel_videos = []

# User login/signup
new_account = input("Do you have a channel: (Y for yes, N for no) ")

if new_account == "Y":
    channel_name = input("Enter your channel name: ")
    channel_number_of_subscribers = lib.backend.get_channel_subscriber_number(channel_name)
    channel_videos = lib.backend.get_channel_videos(channel_name)

elif new_account == "N":
    channel_name = input("Enter your new channel name: ")

# Main event loop
print("What would you like to do? ")
print("- view channel data")
print("- read file")
action = input()
if action == "view channel data":
    channel = input("Enter channel name: ")
    print("What would you like to see?")
    print("- name")
    print("- subs")
    print("- videos")
    action_1 = input()
    if action_1 == "name":
        lib.backend.get_channel_name(channel)
    elif action_1 == "subs":
        lib.backend.get_channel_subscriber_number(channel)
    elif action_1 == "videos":
        lib.backend.get_channel_videos(channel)
    print("Would you like to sub to channel? (Y = yes, N = no)")
    action_2 = input()
    if action_2 == "Y":
        lib.backend.subscribe_to_channel(channel)
        print("Subscribed.")


elif action == "read file":
    file_name = input("Input file name")
    lib.backend.read_file_as_list(file_name)



# Save session information
if new_account == "Y":
    # Update the existing channel file
    lib.backend.update_existing_channel(channel_name, channel_number_of_subscribers, channel_videos)
elif new_account == "N":
    # Create a textfile with the channel information
    lib.backend.create_channel(channel_name, channel_number_of_subscribers, channel_videos)