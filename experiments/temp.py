import os








# if os.system("nc -z locahost 9092")==0:
#     print("kat gaya")
# if os.system("nc -z locahost 2181")==0:
#     print("ek aur baar")
# # while True:
#     continue


if __name__ == "__main__":
    # connectZookeeper()
    # time.sleep(20)
    # connectKafkaServer()
    # time.sleep(10)
    # printAllTopics()
    # killKafkaServer()
    # time.sleep(5)
    # killZookeeper()
    # time.sleep(5)
    connectToCouchbaseAndUpsertNRecords()
    print("All done")
