import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import time

c = 0

def dist(p1, p2):
    # menghitung jarak antara dua titik dalam ruang 3D
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

def brute_force(points):
    # pencarian sepasang titik terdekat dengan algoritma brute force
    min_dist = float('inf')
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            d = dist(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])
    return pair, min_dist

def find_closest_pair(points):
    global c
    # pencarian sepasang titik terdekat dengan algoritma divide and conquer
    def divide_conquer(points_x, points_y):
        n = len(points_x)
        global c
        if n <= 3:
            return brute_force(points_x)
        else:
            mid = n // 2
            mid_point = points_x[mid][0]
            points_y_left = [p for p in points_y if p[0] < mid_point]
            points_y_right = [p for p in points_y if p[0] >= mid_point]
            pair_left, dist_left = divide_conquer(points_x[:mid], points_y_left)
            pair_right, dist_right = divide_conquer(points_x[mid:], points_y_right)
            if dist_left < dist_right:
                closest_pair = pair_left
                closest_dist = dist_left
            else:
                closest_pair = pair_right
                closest_dist = dist_right
            strip_points = [p for p in points_y if abs(p[0] - mid_point) < closest_dist]
            strip_n = len(strip_points)
            for i in range(strip_n):
                j = i + 1
                while j < strip_n and strip_points[j][1] - strip_points[i][1] < closest_dist:
                    d = dist(strip_points[i], strip_points[j])
                    c += 1
                    if d < closest_dist:
                        closest_dist = d
                        closest_pair = (strip_points[i], strip_points[j])
                    j += 1
            return closest_pair, closest_dist
        
    points = sorted(points, key=lambda x: x[0])
    points_y = sorted(points, key=lambda x: x[1])
    return divide_conquer(points, points_y)[0]

# input

def tigaDimensi():
    print("")
    print("")
    n = int(input("Masukkan jumlah titik: "))
    points = np.array([[random.randint(-1000, 1000), random.randint(-1000, 1000), random.randint(-1000, 100)] for i in range(n)])

    # cari sepasang titik terdekat dengan algoritma brute force
    start_time = time.time()
    brute_pair, brute_dist = brute_force(points)
    end_time = time.time()
    banyakOPBrute = len(points)*(len(points)-1)/2

    print("")
    print("BRUTE FORCE")
    print("Brute Force Pair : ", brute_pair)
    print("Banyaknya operasi perhitungan :", banyakOPBrute)
    print("Jarak : ", brute_dist)
    print("Waktu eksekusi : ", end_time - start_time, "detik")

    # cari sepasang titik terdekat dengan algoritma divide and conquer
    start_time = time.time()
    divcon_pair = find_closest_pair(points)
    divcon_dist = dist(divcon_pair[0], divcon_pair[1])
    end_time = time.time()

    print("")
    print("")
    print("DIVIDE AND CONQUER")
    print("Divide and Conquer Pair : ", divcon_pair)
    print("Banyaknya operasi perhitungan :", c)
    print("Jarak : ", divcon_dist)
    print("Waktu eksekusi : ", end_time - start_time, " detik")

    # BONUS 1
    # plot semua titik dalam bidang 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:,0], points[:,1], points[:,2], c='g', marker='o')

    # plot sepasang titik terdekat dengan algoritma brute force
    ax.plot([brute_pair[0][0], brute_pair[1][0]], [brute_pair[0][1], brute_pair[1][1]], [brute_pair[0][2], brute_pair[1][2]], c='r')

    # plot sepasang titik terdekat dengan algoritma divide and conquer
    ax.plot([divcon_pair[0][0], divcon_pair[1][0]], [divcon_pair[0][1], divcon_pair[1][1]], [divcon_pair[0][2], divcon_pair[1][2]], c='r')

    plt.show()

def nDimensi():
    # BONUS 2
    n = int(input("Masukkan jumlah titik : "))
    dim = int(input("Masukkan dimensi : "))
    points = np.array([[random.randint(-1000, 1000) for i in range(dim)] for j in range(n)])

    # cari sepasang titik terdekat dengan algoritma brute force
    start_time = time.time()
    brute_pair, brute_dist = brute_force(points)
    end_time = time.time()
    banyakOPBrute = len(points)*(len(points)-1)/2

    print("")
    print("BRUTE FORCE")
    print("Brute Force Pair : ", brute_pair)
    print("Banyaknya operasi perhitungan :", banyakOPBrute)
    print("Jarak : ", brute_dist)
    print("Waktu eksekusi : ", end_time - start_time, "detik")

    start_time = time.time()
    divcon_pair = find_closest_pair(points)
    divcon_dist = dist(divcon_pair[0], divcon_pair[1])  
    end_time = time.time()

    print("")
    print("DIVIDE AND CONQUER")
    print("Divide and Conquer Pair : ")
    for i in range(n):
        for j in range(i+1, n) :
            if divcon_dist == dist(points[i], points[j]):
                print( "(", points[i],") dan (", points[j],")")
                break
        else:
            continue
        break
    print("Jarak: ", divcon_dist)
    print ("Banyaknya operasi perhitungan: ", c)
    print("Waktu eksekusi: ", end_time - start_time, "detik")

    # BONUS 1
    # plot semua titik dalam bidang 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:,0], points[:,1], points[:,2], c='g', marker='o')

    # plot sepasang titik terdekat dengan algoritma brute force
    ax.plot([brute_pair[0][0], brute_pair[1][0]], [brute_pair[0][1], brute_pair[1][1]], [brute_pair[0][2], brute_pair[1][2]], c='r')

    # plot sepasang titik terdekat dengan algoritma divide and conquer
    ax.plot([divcon_pair[0][0], divcon_pair[1][0]], [divcon_pair[0][1], divcon_pair[1][1]], [divcon_pair[0][2], divcon_pair[1][2]], c='r')

    plt.show()


def main():
    while True:
        print("==============================================================================")
        print("Program Mencari Pasangan Titik Terdekat 3D dengan Algoritma Divide and Conquer")
        print("==============================================================================")
        print("1. 3 Dimensi")
        print("2. n Dimensi")
        print("3. Keluar")
        pilihan = int(input("Masukkan pilihan: "))
        if pilihan == 1:
            tigaDimensi()
        elif pilihan == 2:
            nDimensi()
        elif pilihan == 3:
            print("Terima kasih")
            break
        else:
            print("Pilihan tidak valid")


main()