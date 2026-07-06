class DynamicArray {
private:
int* arr;
int length;
int capacity;
public:

    DynamicArray(int capacity) {
        this->capacity = capacity;
        length = 0;
        arr = new int[capacity];
        

    }

    int get(int i) {
        return arr[i];

    }

    void set(int i, int n) {
        arr[i] = n;

    }

    void pushback(int n) {
        if (length == capacity){
            resize();
        }
        arr[length] = n;
        length++;

    }

    int popback() {
        length --;
        return arr[length];
        

    }

    void resize() {
        int newcap = capacity*2;
        int* newarr = new int[newcap];
        for (int i = 0; i < length; i++) {
            newarr[i] = arr[i];
        }
        delete[] arr;
        arr = newarr;
        capacity = newcap;


    }

    int getSize() {
        return length;
    }

    int getCapacity() {
        return this->capacity;

    }
};
