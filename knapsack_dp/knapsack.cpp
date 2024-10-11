#pragma optimize GCC ("Ofast")
#pragma optimize GCC ("unroll-loops")
#include <bits/stdc++.h>

const int inf = 1e9;
const int N_MAX = 1000;
const int MAX_WEIGHT = 210000;

int dp[MAX_WEIGHT][N_MAX][2];
bool taken[MAX_WEIGHT][N_MAX][2];

using namespace std;

int main() {

    const char* filename_in = "input.txt";
    const char* filename_out = "output.txt";
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    freopen(filename_in, "r", stdin);
    freopen(filename_out, "w", stdout);

    int n, b;
    cin >> n >> b;
    int a[n + 1], c[n + 1];
    for (int i = 1; i <= n; ++i) {
        cin >> a[i] >> c[i];
    }

    for (int w = 1; w <= b; ++w) {
        for(int f = 0; f < 2; ++f){
            dp[w][0][f] = -inf;
        }
    }
    for(int i = 0; i <= n; ++i) {
        dp[0][i][1] = -inf;
    }

    for(int w = 1; w <= b; ++w) {
        for(int i = 1; i <= n; ++i) {
            for(int f = 0; f < 2; ++f) {
                dp[w][i][f] = dp[w][i - 1][f];
                if (w >= a[i] && dp[w - a[i]][i - 1][f ^ 1] + c[i] > dp[w][i][f]) {
                    dp[w][i][f] = dp[w - a[i]][i - 1][f ^ 1] + c[i];
                    taken[w][i][f] = true;
                }
            }
        }
    }


    int best_cost = 0, weight = 0;
    int x[n + 1] = {0};

    for (int w = 1; w <= b; ++w) {
        if(dp[w][n][1] > best_cost) {
            best_cost = dp[w][n][1];
            weight = w;
        }

    }

    if (weight == 0) {
        cout << "No solution\n";
    }

    int fl = 1, total_cost = 0, kol = 0, total_weight = weight;
    for (int i = n; i >= 1; i--) {
        if(taken[weight][i][fl]) {
            x[i] = true;
            weight -= a[i];
            total_cost += c[i];
            kol++;
            fl ^=1;
        }
    }

    cout << best_cost << ' ' << kol << ' ' << total_cost <<  ' ' << total_weight << '\n';
    for (int i = 1; i <= n; ++i) {
        cout << x[i] << ' ';
    }
    return 0;
}

/* Simple Test
 6 15
 2 5
 3 7
 7 5
 4 3
 7 9
 2 4
*/
