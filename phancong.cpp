// DINH QUANG TRUONG - 3115410174

#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;

int matrix_task[100][100];
int array_job[100];
int qty_machines;
int qty_jobs;

void init(){
    ifstream input("file_input.txt");

    input >> qty_machines;
    input >> qty_jobs;
    
    for (int i = 0 ; i < qty_jobs; i++){
        input >> array_job[i];
    }
    
    sort(array_job, array_job + qty_jobs, greater<int>());
}

int select_machine(int index_job){
    int min = 1000000;
    int index = 0;
    for(int order_machine = 0; order_machine < qty_machines; order_machine ++){
        int total = 0;
        for (int old_job = 0; old_job < index_job; old_job++){
            total += matrix_task[order_machine][old_job];
        }
        if (total < min){
            min = total;
            index = order_machine;
        }
    }
    return index;
}

void assign_machine(){
    for(int job = 0; job < qty_jobs; job++){
        int index_machine = select_machine(job);
        matrix_task[index_machine][job] = array_job[job];
    }
}

int get_min_time(){
    int max = 0;
    for(int order_machine = 0; order_machine < qty_machines; order_machine ++){
        int total = 0;
        for (int old_job = 0; old_job < qty_jobs; old_job++){
            total += matrix_task[order_machine][old_job];
        }
        if (total > max){
            max = total;
        }
    }
    return max;
}

int main(){
    init();
    assign_machine();
    for (int i =0 ;i < qty_machines; i++){
        for(int j =0 ; j < qty_jobs; j++){
            cout<<matrix_task[i][j] << "   ";
        }
        cout<<"\n";
    }
    cout << "Time min: " << get_min_time();
}