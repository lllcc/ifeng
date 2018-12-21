# encoding: utf-8
from rediscluster import StrictRedisCluster
import sys


# redis_nodes = [{"host": "10.80.23.175", "port": 7000},
#                {"host": "10.80.23.175", "port": 7001},
#                {"host": "10.80.24.175", "port": 7000},
#                {"host": "10.80.24.175", "port": 7001},
#                {"host": "10.80.25.175", "port": 7000},
#                {"host": "10.80.25.175", "port": 7001}
#                ]


def redis_cluster(pos):
    redis_nodes = [{"host": "10.32.0.20", "port": 7000},
                   {"host": "10.32.0.20", "port": 7001},
                   {"host": "10.32.0.14", "port": 7000},
                   {"host": "10.32.0.14", "port": 7001},
                   {"host": "10.32.0.27", "port": 7000},
                   {"host": "10.32.0.27", "port": 7001},
                   {"host": "10.32.0.6", "port": 7000},
                   {"host": "10.32.0.6", "port": 7001},
                   {"host": "10.32.0.18", "port": 7000},
                   {"host": "10.32.0.18", "port": 7001},
                   {"host": "10.32.0.15", "port": 7001},
                   {"host": "10.32.0.15", "port": 7000},
                   {"host": "10.32.0.16", "port": 7001},
                   {"host": "10.32.0.16", "port": 7000},
                   {"host": "10.32.0.26", "port": 7001},
                   {"host": "10.32.0.26", "port": 7000},
                   {"host": "10.32.0.7", "port": 7001},
                   {"host": "10.32.0.7", "port": 7000},
                   {"host": "10.32.0.3", "port": 7001},
                   {"host": "10.32.0.3", "port": 7000},
                   {"host": "10.32.0.25", "port": 7001},
                   {"host": "10.32.0.25", "port": 7000},
                   {"host": "10.32.0.17", "port": 7001},
                   {"host": "10.32.0.17", "port": 7000}
                   ]
    # redis_nodes = [{"host": "10.80.23.175", "port": 7000},
    #                {"host": "10.80.23.175", "port": 7001},
    #                {"host": "10.80.24.175", "port": 7000},
    #                {"host": "10.80.24.175", "port": 7001},
    #                {"host": "10.80.25.175", "port": 7000},
    #                {"host": "10.80.25.175", "port": 7001}
    #                ]
    try:
        redisconn = StrictRedisCluster(startup_nodes=redis_nodes,
                                       skip_full_coverage_check=True)
    except Exception as e:
        print("Connect Error!")
        sys.exit(1)
    for ss in pos:
        redisconn.delete(ss, 1)
    print("end")


def read_file():
    # file_name = "D:\data\logs\hippo.log"
    file_name = "/data/ip.txt"
    pos = []
    with open(file_name, 'r') as file_to_read:
        while True:
            lines = file_to_read.readline()
            if not lines:
                break
                pass
            lines = lines.replace("\n", "")
            pos.append(lines)  # 添加新读取的数据
            pass
        # pos = np.array(pos)  # 将数据从List类型转化为array类型
        pass
    return pos


p = read_file()
redis_cluster(p)
