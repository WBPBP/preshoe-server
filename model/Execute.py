import sys
import json
import random
from StaticPlantarPressureResAnalysis import analysisStaticPressureResult
from GaitAnalysis import walkCheck


def run(verticalWeightBias_Left, verticalWeightBias_Right, horizontalWeightBias, heelPressureDifference, leftPressure, rightPressure) :
    staticPressureRes = analysisStaticPressureResult(verticalWeightBias_Left, verticalWeightBias_Right, horizontalWeightBias, heelPressureDifference);
    score, gaitComment, diseaseNum = walkCheck(leftPressure, rightPressure)
    dict = {"staticPressureRes": staticPressureRes, "percent": score, "gaitComment": gaitComment, "diseaseNum": diseaseNum}
    print(json.dumps(dict, ensure_ascii=False))
    #json으로 형식 변환


# 실제 사용시에 입력받을 부분입니다.
# 입력값 6개 들어옴 
json_data=sys.argv[1]
data=json.loads(json_data)
verticalWeightBias_Left = data['verticalWeightBias_Left']
verticalWeightBias_Right = data['verticalWeightBias_Right']
horizontalWeightBias = data['horizontalWeightBias']
heelPressureDifference = data['heelPressureDifference']
leftPressure = data['leftPressure']
rightPressure = data['rightPressure']

if len(leftPressure)==120 and len(rightPressure) == 120:
    f = open("/home/ec2-user/myapp/model/GaitData.txt", 'a')
    f. write("left : " + str(leftPressure) + "\n")
    f. write("right : " + str(rightPressure) + "\n\n")
    f.close()

'''
# 더미 데이터 생성
verticalWeightBias_Left = random.random()
verticalWeightBias_Right = random.random()
horizontalWeightBias = random.random()
heelPressureDifference = random.randint(0, 60)
leftPressure = [1,2,3]
rightPressure = [1,2,3]

for i in range(120):
	leftPressure.append(random.randint(0, 16))
	rightPressure.append(random.randint(0, 16))
'''


#실행 함수 호출
run(verticalWeightBias_Left, verticalWeightBias_Right, horizontalWeightBias, heelPressureDifference, leftPressure, rightPressure)


