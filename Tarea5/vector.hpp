#include <iostream>
#include <vector>
#include <list>
using namespace std;

namespace myvec{
	class Vector{
		private:
			int pos1;
                        int pos2;
                        int pos3;
                        int pos4;
                        int pos5;
		public:	
			std::vector<int> v;
			
   
			int GetSize(){ //Devuelve el size del vector
				return v.size();

			}

			Vector(int n){    //inicializa un vector con n component  
                                for (int i=1;i<=n;i++){
                                        v.push_back(0);
                                } //Crea vectores de n elementos
                            pos1=0;
                        	pos2=0;
                        	pos3=0;
                        	pos4=0;
                        	pos5=0;
                        }
			
		
			//Cargando[]
			int &operator[](int i) {
        			if( i > v.size() ) {
            				cout << "Index out of bounds" <<endl; 
            		// return first element.
            				return v[0];
         			}
			
         			return v[i];
      			}

			//Cargando +
			Vector operator+(const Vector& obj) {

         			Vector box(v.size());
				box.pos1=this->pos1+obj.pos1;
				box.pos2=this->pos2+obj.pos2; 
				box.pos3=this->pos3+obj.pos3; 
				box.pos4=this->pos4+obj.pos4; 
				box.pos5=this->pos5+obj.pos5;
				box[0]=box.pos1;
				box[1]=box.pos2;
				box[2]=box.pos3;
				box[3]=box.pos4;
				box[4]=box.pos5;

         			return box;

			}

			Vector operator-(const Vector& obj) {

                                Vector box(v.size());
                                box.pos1=this->pos1-obj.pos1;
                                box.pos2=this->pos2-obj.pos2;
                                box.pos3=this->pos3-obj.pos3;
                                box.pos4=this->pos4-obj.pos4;

                                box[0]=box.pos1;
                                box[1]=box.pos2;
                                box[2]=box.pos3;
                                box[3]=box.pos4;
				box[4]=box.pos5; 
                                return box;

                        }		
			void operator = (const Vector &D ) {
				pos1=D.pos1;
				pos2=D.pos2;
				pos3=D.pos3;
				pos4=D.pos4;
				pos5=D.pos5; 
         			v[0] = pos1;
				v[1] = pos2;
				v[2] = pos3;
				v[3] = pos4;
				v[4] = pos5;

				         	
      			}

			void PrintVec() {    //Imprime las componentes del vector
				for (int i=0;i<v.size();i++){
					cout << v[i] << endl;
				
				}

			 }

			int SetPos(int a,int b){  //LLena la posición a del vector con b
				v[a]=b;
				if (a==0){
					pos1=b;
				}
				if (a==1){
					pos2=b;
				}
				if (a==2){
					pos3=b;
				}
				if (a==3){
					pos4=b;
				}
				if (a==4){
					pos5=b;
				}
				return 0;
			}



			int GetPos(int n){
		
				return v[n];
			}


};

}



