# Using Set for tracking active users in a chat room
def manage_chat_room(active_users: set, action: str, user: str) -> set:
  if action == 'join':
      active_users.add(user)
  elif action == 'leave':
      active_users.discard(user) #won't raise error if not found
  return active_users

def get_user_status(active_users: set, user: str) -> str:
  return f"{user} is {'active' if user in active_users else 'inactive'}"
