import argparse
from webcam_utils import run_realtime_emotion
from prediction_utils import prediction_path

# for running realtime emotion detection
def realtime_emotion():
    prepare_realtime_emotions()
    run_realtime_emotion()

# to run emotion detection on image saved on disk
def run_detection_path(path):
    prediction_path(path)


def main():
    realtime_emotion()
    # parser = argparse.ArgumentParser()
    # parser.add_argument("func_name", type=str,
    #                     help="Select a function to run. <emo_realtime> or <emo_path>")
    # parser.add_argument("--path", default="saved_images/1.jpg", type=str,
    #                     help="Specify the complete path where the image is saved.")
    # # parse the args
    # args = parser.parse_args()

    # #print('****ARGS: ' + str(args))

    # if args.func_name == "emo_realtime":
    #     run_realtime_emotion()
    # elif args.func_name == "emo_path":
    #     run_detection_path(args.path)
    # else:
    #     print("Usage: python main.py <function name>")

if __name__ == '__main__':
    main()
