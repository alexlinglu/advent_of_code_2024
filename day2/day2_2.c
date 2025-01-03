#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

void remove_element(int *array, int index, int array_length)
{
   int i;
   for(i = index; i < array_length - 1; i++) array[i] = array[i + 1];
}

bool checkSafety(int *arr, int reports, bool removed){
    int k;
    if(arr[0] > arr[1]){
        for(k = 0; k < reports - 1; k++){
            printf(" sorted? %d", arr[k]);
            if(arr[k] <= arr[k + 1] || 3 < abs(arr[k] - arr[k + 1])){
                if(removed){
                    printf(" break %d! ", arr[k + 1]);
                    return false;
                } else{
                    int removed_level[10];
                    int removed_level2[10];
                    printf(" sorted1.2 %d! ", arr[k + 1]);
                    memcpy(removed_level, arr, (reports * sizeof(int)));
                    memcpy(removed_level2, arr, (reports * sizeof(int)));
                    remove_element(removed_level, k + 1, reports);
                    remove_element(arr, 0, reports);
                    remove_element(removed_level2, 1, reports);
                    return (checkSafety(removed_level, reports - 1, true) || checkSafety(arr, reports - 1, true) || checkSafety(removed_level2, reports - 1, true));
                }
            }
        }
    } else{
        for(k = 0; k < reports - 1; k++){
            printf(" sorted2? %d", arr[k]);
            if(arr[k] >= arr[k + 1] || 3 < abs(arr[k] - arr[k + 1])){
                if(removed){
                    printf(" break %d! ", arr[k + 1]);
                    return false;
                } else{
                    int removed_level[10];
                    int removed_level2[10];
                    printf(" sorted2.2 %d! ", arr[k + 1]);
                    memcpy(removed_level, arr, (reports * sizeof(int)));
                    memcpy(removed_level2, arr, (reports * sizeof(int)));
                    remove_element(removed_level, k + 1, reports);
                    remove_element(arr, 0, reports);
                    remove_element(removed_level2, 1, reports);
                    return (checkSafety(removed_level, reports - 1, true) || checkSafety(arr, reports - 1, true) || checkSafety(removed_level2, reports - 1, true));
                }
            }
        }
        return true;
    }
}

int main(int argc, char **argv){
    FILE* file = fopen("input.txt", "r");
    char line[256];
    int i;
    int count = 0;
    if(file != NULL){
        for(i = 0; i < 1000; i++){
            char * number;
            int level[10];
            int reports = 0;
            if(fgets(line, sizeof(line), file)){
                number = strtok(line, " ");
                int j = 0;
                printf("\nnumber:%s", number);
                while(number != NULL){
                    reports ++;
                    level[j] = atoi(number);
                    number = strtok (NULL, " ");
                    j++;
                }
                if(checkSafety(level, reports, false)){
                    count++;
                    printf(" counted!");
                } else{
                    printf(" not counted!");
                }
            }
        }
        printf("\n%d", count);
        fclose(file);
    } else{
        fprintf(stderr, "Unable to open file\n");
    }
    return 0;
}