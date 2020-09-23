/**
 * quick sort
 * 
 * time: O(nlogn)
 *      每一轮的比较和交换，需要把数组全部元素都遍历一遍，时间复杂度是O(n)，那么平均情况下需要logn轮，所以平均时间复杂度是O(nlogn)。
 * 分治: 一轮挑选一个基准元素，并让其他比它大的元素移动到数列一边，比它小的元素移动到数列的另一边，从而把数列拆解成两个部分。
 * 
 * 注1：数列的第1个元素要么是最小值，要么是最大值，就无法发挥分治法的优势。
 * 解1：随机选择基准元素。
 * 
 * 注2：为了不使用辅助空间，使用指针方式交换位置。
 * 解2：双边循环法/单边循环法
 */

#include <iostream>

// #include <ctime>

using namespace std;


template <typename T>
void quick_sort(T& array, int start, int end){
    // 递归结束条件
    if(start >= end){
        return;
    }

    int pivot = start;
    int left = start;
    int right = end;

    // 使用随机选取基准
    // srand((int)time(0));
    // pivot = rand() % (end - start) + start;
    // swap(array[start], array[pivot]);   // 把基准放在首个元素
    // pivot = start;

    // 双边循环法
    while(left < right){
        if(array[right] > array[pivot]){
            right--;
            continue;
        }
        if(array[left] <= array[pivot]){
            left++;
            continue;
        }else{
            swap(array[left], array[right]);
        }
    }

    // 交换基准和第一个元素
    swap(array[pivot], array[left]);
    pivot = left;

    // 递归
    quick_sort(array, start, pivot);
    quick_sort(array, pivot+1, end);
}


int main(int argc, char const *argv[])
{
    // int list[]{};
    // int list[]{5};
    // int list[]{5, 6};
    int list[]{5, 6, 3, 8, 2, 1, 7, 9};

    quick_sort(list, 0, end(list)-begin(list)-1);

    for(auto li : list){
        cout << li << " ";
    }
    cout << endl;
    
    return 0;
}