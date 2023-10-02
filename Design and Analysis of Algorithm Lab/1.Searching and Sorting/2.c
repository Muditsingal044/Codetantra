#include<stdio.h>

int binary(int array[] , int l , int h , int v){
  if(l<=h){
     int m = (l+h)/2;
  if (array[m]==v){
      return 1;
      }
  else if (array[m]<v){
      return binary(array,m+1,h,v);
      }
    return binary(array,l,m-1,v);
      }
    return 0;
    }

int main(){
    int a,b;
    printf("Enter number of elements: ");
    scanf("%d",&a);
    print("Enter the sorted array: ");
    int array[a];
    for(int i=0;i<a;i++){
        scanf("%d",&array[i]);
        }
    printf("enter the item to be search: ");
    scanf("%d",&b);
    int ans = binary(array , 0 , a-1 , b);
  
    if (ans==0){
      printf("item not present");
    }

    else{
       printf("item present");
    }
   return 0;
}

  
