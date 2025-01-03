#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

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
                int k;
                bool safe = true;
                if(level[0] > level[1]){
                    for(k = 0; k < reports - 1; k++){
                        printf(" sorted? %d ", level[k]);
                        if(level[k] <= level[k + 1] || 3 < abs(level[k] - level[k + 1])){
                            safe = false;
                            printf("break %d", level[k + 1]);
                            break;
                        }
                    }
                } else{
                    for(k = 0; k < reports - 1; k++){
                        printf(" sorted2? %d ", level[k]);
                        if(level[k] >= level[k + 1] || 3 < abs(level[k] - level[k + 1])){
                            safe = false;
                            printf("break %d", level[k + 1]);
                            break;
                        }
                    }
                }
                if(safe){
                    count++;
                    printf("counted!");
                }
            }
        }
        printf("%d", count);
        fclose(file);
    } else{
        fprintf(stderr, "Unable to open file\n");
    }
    return 0;
}