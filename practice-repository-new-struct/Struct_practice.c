#include <stdio.h>

    struct fraction {
        int numerator;
        int denominator;
    };

int main(){

    struct fraction fract1, fract2;
    
    //new comment
    fract1.numerator = 2200;
    fract1.denominator = 7;
    fract2 = fract1;

    printf("%d / %d\n", fract1.numerator, fract1.denominator);
    printf("%d / %d", fract2.numerator, fract2.denominator);
    
}
