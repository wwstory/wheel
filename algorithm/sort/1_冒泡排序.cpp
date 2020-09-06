/**
 * bubble sort
 * 
 * time: O(n^2)
 */

#include <iostream>

using namespace std;

template <typename T>
void swap(T& a, T& b){
    T c = a;
    a = b;
    b = c;
}

template <typename T>
T& bubble_sort(T& list){
    // get length
    int length = sizeof(list) / sizeof(list[0]);
    // bubble
    for(int i = 0; i < length; i++){
        for(int j = 0; j < length-i-1; j++){
            if(list[j] > list[j+1]){    // swap
                ::swap(list[j], list[j+1]); // 与std标准库冲突，加::
            }
        }
    }

    return list;
}

int main(int argc, char const *argv[])
{
    // int list[]{};
    // int list[]{5};
    // int list[]{5, 6};
    int list[]{5, 6, 3, 8, 2, 1, 7, 9};
    // int* list = new int[8]{5, 6, 3, 8, 2, 1, 7, 9}; // 不能使用for-each

    bubble_sort(list);

    // int length = end(list) - begin(list);
    // for(auto li = list; li != list+length; li++){
    //     cout << *li << " ";
    // }
    for(auto li : list){
        cout << li << " ";
    }
    cout << endl;

    
    return 0;
}
