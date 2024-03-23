#include <iostream>
using namespace std;

class Count
{
    int s = 0;

public:
    ~Count(); // ���������������ڵ�16��

    Count(int s) { this->s = s; } // ���캯��
    int getS() { return s; }
    void sPlus() { s++; }
};

Count::~Count() { cout << this->s << " "; } // ���s

// ���ù��캯��
Count count5(555);
static Count count6(666);
Count count7(777);

void f() { static Count count9(999); }

int main()
{
    Count *count1 = new Count(111);
    Count *count2 = new Count(222);

    Count count3(333);
    Count count4(444);

    f(); // ��̬������������f()�൱�������滻һ���Ź���

    static Count count8(888);

    delete (count1);

    for (int i = 1; i <= 5; i++)
        for (Count c(1); c.getS() <= i; c.sPlus())
            ; // ��Щ������ֻ��һ�仰�������Σ������滻������Ϊ�˳���д�ķ�������
    return 0;
}

/* �������������ĵ��ã������ڿ��칹�캯������������

����Դ�����е�ע�ͣ�����ֱ�Ӵ�main��������
��ͷһ������������Ȳ��ܣ���Ϊ���Ƕ�û���꣬��������������

37�У��ͷ�count1, ����������������� 111
39������ѭ����i = 1
40�����캯��������Ϊc�����μ�sΪ1������ѭ��ʱsΪ2��c����ʹ����ϣ��ͷţ����2����ѭ��֪�������3 4 5 6 ��

ѭ��������main����Ҳ�ͽ����ˣ�����ʱȫ�ֺ;�̬�����Ļ������ͷţ��������빹��˳���෴�������444 333
��222���������Ϊ���������Լ�ȡ�Ŀռ䣬ֻ���ֶ��ͷŻ�����������������������ͷţ�
ʣ�µ�ͬ��˳���෴��888 999 777 666 555

 */
