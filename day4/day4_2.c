#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool findmas(int row, int column, char map[140][140]){
    bool first = false;
    bool second = false;
    if(row == 0 || row == 139 || column == 0 || column == 139){
        return false;
    } 
    if(map[row - 1][column - 1] == 'M' && map[row + 1][column + 1] == 'S' || map[row - 1][column - 1] == 'S' && map[row + 1][column + 1] == 'M'){
        first = true;
    }
    if(map[row - 1][column + 1] == 'M' && map[row + 1][column - 1] == 'S' || map[row - 1][column + 1] == 'S' && map[row + 1][column - 1] == 'M'){
        second = true;
    }
    //printf("%d%d", first, second);
    return (first && second);
}

int main(int argc, char **argv){
    char line[256];
    char puzzleMap[140][140];
    int i = 0;
    int j, k, l, m, n;
    int count = 0;
    FILE* file = fopen("input.txt", "r");
    if(file != NULL){
        while(fgets(line, sizeof(line), file) != NULL){
            for(n = 0; n < 140; n++){
                puzzleMap[i][n] = line[n];
            }
            i++;
        }
        fclose(file);
    } else{
        fprintf(stderr, "Unable to open file\n");
    }
    for(j = 0; j < 140; j++){
        //printf("%d:\n", j);
        for(k = 0; k < 140; k++){
            if(puzzleMap[j][k] == 'A'){
                //printf("A!");
                if(findmas(j, k, puzzleMap)){
                    //printf(" counted!\n");
                    count++;
                } 
                //else{ printf(" not counted!\n");}
            }
        }
    }
    printf("%d", count);
    return 0;
}