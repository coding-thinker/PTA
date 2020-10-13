#include <cstdio>
#include <vector>
#define INF 65535
using namespace std;


// Cpp version for 1003 Emergency.py
// Accpeted on all 6 cases

class Citys{
    public:
    vector<vector<int>> map;    
    vector<int> teams;
    int size;
    int minimum = INF;
    int mans = 0;
    int src = -1;
    int dst = -1;
    int num = 0;
    vector<int> used;

    void init(){
        int size;
        int lines;
        scanf("%d %d %d %d", &size, &lines, &this->src, &this->dst);
        this->set_size(size);
        this->set_teams();
        this->set_edge(lines);
    }

    bool find(int v){
        for(int i = 0; i < this->used.size(); ++i){
            if(this->used[i] == v){
                return true;
            }
        }
        return false;
    }

    void set_size(int size){
        this->size = size;
        this->teams.resize(size);
        this->map.resize(size);
        for(int i=0; i<size; i++){
            this->map[i].resize(size);
        }
        for(int i=0; i<size; i++){
            for(int j=0; j<size; j++){
                map[i][j] = INF;
            }
        }
    }

    void set_edge(int m){
        int a, b, v;
        for(int i = 0; i < m; ++i){
            scanf("%d %d %d", &a, &b, &v);
            this->map[a][b] = v;
            this->map[b][a] = v;
        }

    }

    void set_teams(){
        int team;
        for(int i = 0; i < this->size; ++i){
            scanf("%d", &team);
            this->teams[i] = team;
        }
    }

    void dfs(int paths, int mans){
        if(!this->used.empty()){
            if(this->used[this->used.size()-1] == this->dst){
                if(this->minimum > paths){
                    this->num = 1;
                    this->minimum = paths;
                    this->mans = mans;
                }else if (this->minimum == paths){
                    this->num++;
                    if(this->mans < mans){
                        this->mans = mans;
                    }
                }
                return ;
            }
        }
        {
            if(!this->used.empty()){
                int temp;
                for(int each = 0; each < this->size; each++){
                    if(find(each)) continue;
                    temp = this->map[this->used[this->used.size()-1]][each];
                    if(temp >= INF) continue;
                    temp += paths;
                    if( this->minimum < temp) continue;
                    if(temp <= this->minimum){
                        used.push_back(each);
                        this->dfs(temp, mans + this->teams[each]);
                        used.pop_back();
                    }
                }
            }
            else{
                used.push_back(this->src);
                this->dfs(paths , mans + this->teams[this->src]);
            }
        }
    }

    
    
};

int main(){
    Citys city;
    city.init();
    city.dfs(0, 0);
    printf("%d %d", city.num, city.mans);
}