#include <iostream>
using namespace std;

int main() {
	char s{0};
	int a{0}, c{0}, t{0}, g{0};
	cin >> s;
	while(!(cin.eof())) {
		if (s == 'A') ++a;
		else if (s == 'C') ++c;
		else if (s == 'T') ++t;
		else if (s == 'G') ++g;
		cin >> s;
	}
	cout << a << " "<< c << " " << g << " " << t << endl;
	return 0;
}