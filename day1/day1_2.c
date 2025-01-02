#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * copySubstring(char *dest, const char *src, int start, int end){
    /* copy the substring */
    strncpy(dest, src + start, end - start);

    /* add null since strncpy probably didn't */
    dest[end - start] = '\0';

    return dest;
}
int countInRight(int n, int* array){
    int count = 0;
    int k;
    for(k = 0; k < 1000; k++){
        if(n == array[k]){
            count++;
        }
    }
    return count;
}

int main(int argc, char **argv){
    FILE* file = fopen("output.txt", "r");
    char line[256];
    int left[1000];
    int right[1000];
    int sum = 0;
    int i, j, l;
    if(file != NULL){
        for(i = 0; i < 1000; i++){
            if(fgets(line, sizeof(line), file)){
                char first[5];
                left[i] = atoi(copySubstring(first, line, 0, 5));
            }
        }
        for(l = 0; l < 1000; l++){
            if(fgets(line, sizeof(line), file)){
                char second[5];
                right[l] = atoi(copySubstring(second, line, 0, 5));
            }
        }
        for(j = 0; j < 1000; j++){
            int appears = countInRight(left[j], right);
            sum += left[j] * appears;
        }
        printf("%d", sum);
        fclose(file);
    } else{
        fprintf(stderr, "Unable to open file\n");
    }
    return 0;
}
