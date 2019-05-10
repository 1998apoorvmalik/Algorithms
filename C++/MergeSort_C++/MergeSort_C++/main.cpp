//
//  main.cpp
//  MergeSort_C++
//
//  Created by Apoorv Malik on 10/05/19.
//  Copyright © 2019 Apoorv Malik. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;
int count_inv = 0;

// Method 1
void mergeSort(vector<int> &arr) {
    
    if(arr.size() > 1) {
        vector<int> L;
        vector<int> R;
        int mid = int(arr.size())/2;

        for(int i=0;i<mid;i++)
            L.push_back(arr[i]);

        for(int i=mid;i<arr.size();i++)
            R.push_back(arr[i]);

        mergeSort(L);
        mergeSort(R);

// Uncomment the next lines to visualize merge sort tree.
//        for(auto ele: arr)
//            cout<<ele<<" ";
//        cout<<"\n";
//        for(auto ele: L)
//            cout<<ele<<" ";
//        cout<<"\n";
//        for(auto ele: R)
//            cout<<ele<<" ";
//        cout<<"\n\n";

        int i = 0;
        int j = 0;
        int k = 0;

        while(i<int(L.size()) && j<int(R.size())) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            }
            else {
                arr[k] = R[j];
                j++;
                count_inv += (L.size() - i);
            }
            k++;
        }

        while(i<int(L.size())) {
            arr[k] = L[i];
            i++;
            k++;
        }

        while(j<int(R.size())) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }
}

// Another method for merge sort.
// Method 2
void merge(int arr[], int l, int m, int r) {
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;
    
    int L[n1], R[n2];
    
    for(int i=0;i<n1;i++)
        L[i] = arr[l+i];
    
    for(int j=0;j<n2;j++)
        R[j] = arr[m+j+1];
    
    i = 0;
    j = 0;
    k = l;
    
    while (i < n1 && j < n2) {
        
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        }
        else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
    
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
    
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(int arr[], int l, int r) {
    if(l < r) {
        int m = (l+r-1)/2;
        
        mergeSort(arr, l, m);
        mergeSort(arr, m+1, r);
        merge(arr, l, m, r);
    }
}

int main(int argc, const char * argv[]) {
    int size;
    cin>>size;
    
    vector<int> arr;
    int arr1[size];
    
    for(int i=0;i<size;i++) {
        int temp;
        cin>>temp;
        arr.push_back(temp);
        arr1[i] = temp;
    }
    
    mergeSort(arr); // Method 1
    mergeSort(arr1, 0, int(arr.size()) - 1);
    
    cout<<"\nSorted array : ";
    for(auto ele: arr1)
        cout<<ele<<" ";
    
    cout<<"\nNumber of inversions done while sorting : "<<count_inv<<"\n\n";
    return 0;
}
