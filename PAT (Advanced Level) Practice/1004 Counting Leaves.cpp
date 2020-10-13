# include<iostream>
# include<vector>
# include<queue>
using namespace std;

// all accpeted


// new a vector for a new node
void put(vector<vector<int>> &vec, int num){
    vector<int> temp;
    vec[num] = temp;
}

// add child node
void put(vector<vector<int>> &vec, int index,  int num){
    vec[index].push_back(num);
}

class Tree{
    public:
        int N, M;
        queue<int> work_space;
        vector<vector<int>> matrix;

    void set_NM(){
        if(scanf("%d %d", &this->N, &this->M)){};
        this->matrix.resize(N+2);
        for(int i = 0; i <= this->N; ++i){
            put(this->matrix, i);
        }
    }

    void read_input(){
        int num, src, temp;
        for(int i = 0; i < this->M; ++i){
            if(scanf("%d %d", &src, &num)){};
            for(int j = 0; j < num; ++j){
                if(scanf("%d", &temp)){};
                put(this->matrix, src, temp);
            }
        }
    }

    void search(){
        this->work_space.push(1);
        this->work_space.push(-1);
        int num = 0, temp = 0;
        bool root = true;
        while(! this->work_space.empty()){
            num = 0;
            while(this->work_space.front() != -1){ // using -1 as an end-of-layer flag
                temp = this->work_space.front();
                this->work_space.pop();
                if(this->matrix[temp].size()){ //if any child is found push into queue
                    for(auto i: this->matrix[temp]){
                        this->work_space.push(i);
                    }
                }else{
                    num++; //if no child is found count no-child node
                }
            }
            if(root){
                printf("%d", num);
                root = false;
            }else{
                printf(" %d", num);
            }
            this->work_space.pop();
            if(! this->work_space.empty()){
                this->work_space.push(-1);  // push end-of-layer flag
            }else{
                return;
            }
            
        }
    }

};



int main(){
    Tree myTree;
    myTree.set_NM();
    myTree.read_input();
    myTree.search();
    return 0;
}