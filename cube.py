import pyGene

nOfGen = 10; #����ü �� ������ �� 
mOfSpin = 7; #�ּ����� �� 
k = None; #���þ�
generation = [ [[None]*7]*(nOfGen) ]; #���� ����Ʈ
icube = [] #ť�� ����


def fitness(gene): #����ü�� �ѱ�� ���յ��� ��ȯ
    for p in range(mOfSpin) : c = spin(gene[p], icube)
    result = None#c�� ���ؼ� ����/�������� ������??
    return result

def spin(spin, cube): #ȸ�� ���⸦ �ѱ�� ȸ���� ť�긦 ��ȯ cube : ���� ť��
    pass

gen = pyGene.Generation(generation, 2, 1, 0, 0, 0, fitness) #���� ��ü

l = input("�ݺ� Ƚ�� : ")
for i in range(l):
    gen = gen.evol(k)
    print(gen)
    print(i)