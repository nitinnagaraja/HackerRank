#include <bits/stdc++.h>
using namespace std;
#define MAX_SIZE 1000000
struct node {
	int r,c,idx;
};
struct node A[MAX_SIZE];

bool compare(struct node A1,struct node A2){
	if(A1.r < A2.r) return true;
	return false;
}

int n,T[MAX_SIZE]={0};

int modify_BS(int tr){
	int start=0,end=n;
	int mid = (start+end)/2;
	
	while(start <= end){
		if(A[mid].r >= tr && A[mid-1].r < tr ) return mid;
		else if(tr > A[mid].r) start = mid+1;
		else end = mid-1;
		
		mid = (start+end)/2;
	}
	return -1;
}

int find_min_cost_idx(int idx){
	
	int ans = idx;
	for(int j=idx+1;j<n;j++){
		
		if(A[j].c == A[ans].c){
			if(A[j].r ==  A[ans].r) {
				if(A[ans].idx > A[j].idx) ans = j; 
			}
			if(A[j].r > A[ans].r) ans=j;
		}
		
		else if(A[j].c < A[ans].c) { 
			ans = j;
		}
		
		
	}
	return ans;
}

int main() {
	int D,r,c;
	scanf("%d %d",&n,&D);
	for(int i=0;i<n;i++){
		scanf("%d",&A[i].r);
		A[i].idx = i+1;
	}
	for(int i=0;i<n;i++){
		scanf("%d",&A[i].c);
	}
	
	sort(A,A+n,compare);
	
	for(int i=0;i<n;i++){
		printf("%d %d %d\n",A[i].r,A[i].c,A[i].idx);
	}
	
	for(int i=0;i<n;i++){
		int tr = D-A[i].r;
		if(tr < 0) {T[A[i].idx] = 0; continue; }
		printf("tr = %d\n",tr);
		
		int ridx = modify_BS(tr);
		printf("ridx = %d\n",ridx);
		if(ridx != -1){
			int mincostidx = find_min_cost_idx(ridx);
			printf("mincostidx = %d\n",mincostidx);
			T[A[i].idx] = A[mincostidx].idx;
		}
	
		
	}
	
	for(int i=1;i<=n;i++){
		printf("%d ",T[i]);
	}
	printf("\n");

	
	return 0;
}