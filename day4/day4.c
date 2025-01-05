#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool masNext(int rowChange, int columnChange, int letter, int row, int column, char map[140][140]){
    char *remaining = "MAS";
    if(letter == 3){
        //printf("counted! ");
        return true;
    } else
        if(row + rowChange > 139 || row + rowChange < 0 || column + columnChange > 139 || column + columnChange < 0){
            //printf("|| "); //break
            return false;
    } else if(map[row + rowChange][column + columnChange] == remaining[letter]){
        //printf("%c!", remaining[letter]);
        return masNext(rowChange, columnChange, letter + 1, row + rowChange, column + columnChange, map);
    }
    //printf("|  "); //break
    return false;
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
        //printf("%d: ", j);
        for(k = 0; k < 140; k++){
            if(puzzleMap[j][k] == 'X'){
                //printf("X!");
                for(l = -1; l < 2; l++){
                    for(m = -1; m < 2; m++){
                        if(masNext(l, m, 0, j, k, puzzleMap)){
                            count++;
                        }
                    }
                }
                //printf("\n");
            }
        }
        //printf("\n");
    }
    printf("%d", count);
    return 0;
}