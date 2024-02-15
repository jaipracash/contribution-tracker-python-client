from config import uca_client
from actions import contribution_tracker, user_tracker, event_tracker


if __name__ == '__main__':
  uca_client.auto_load_modules()
  uca_client.run_forever()


