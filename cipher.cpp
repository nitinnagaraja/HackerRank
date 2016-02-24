#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <bitset>
#include <cstring>

using namespace std;

void bin(unsigned num, int n) {
    unsigned i;
    for(i = 1 << n-1; i > 0; i = i/2) {
        if (num & i)
	    cout << "1";
	else
	    cout << "0";
    }
    cout << endl;
}

int main() {
    
    int n, k;
    std::string enc_str;
    int enc = 0;
    int dec;

    cin >> n;
    cin >> k;

    cin >> enc_str;

    int exp = n+k-2;

    for(int i = 0; i < n+k-1; i++) {
       char in = enc_str[i];
       if (in == '1') {
           enc += pow(2, exp);
       }
	exp--;
    }

    
    dec = enc & 1;

    int count = 1;

    for(int i = n - 2; i >= 0; i--) {
	int enc_bit = (enc >> count) & 1;
	count++;

	int exor = 0;

	for(int j = i+1; j < i+k; j++) {
	    if(j < n) {
		exor = ((dec >> (n - j - 1)) & 1) ^ exor;
	    }
	}

	if (enc_bit != exor)
	    dec = dec | (1 << (n - i - 1));

    }

    bin(dec, n);
    return 0;
}