#include<stdio.h>

int main(){
    int a,b;
    printf("enter the no of elements: ");
    scanf("%d",&a);
    print("Enter %d integer(s)\n",a);
    int array[a];
    for(int i=0;i<a;i++){
        scanf("%d",&array[i]);
        }
    printf("enter the item to be search: ");
    scanf("%d",&b);
    int f = 0;
    for(int i = 0;i<a;i++){
        if (array[i]==b){
        printf("item location = %d  item = %d",i+1,b);
        f = f+1
        }
     }
    if(f==0){
    printf("no item found");
    }
      return 0;

}

  

