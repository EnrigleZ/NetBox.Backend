from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from TestAPI.models import TestStruct
from TestAPI.serializers import TestStructSerializer

import time
import json
import random

# Create your views here.


def test(request):
    return JsonResponse({'name': 123})


@api_view(['GET', 'POST'])
def createTest(request):
    if request.method == 'GET':
        items = TestStruct.objects.all()
        serializer = TestStructSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # files = request.FILES['file_part']
        # # print(files.size)
        # print(request.data)
        # return JsonResponse({})
        serializer = TestStructSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


PRED_RESPONSE = {"auc": "0.916361454469064", "f1": "0.8721774856203779",
                 "precision": "0.8633524206142634", "recall": "0.8811848309756259"}


@api_view(['POST'])
def pred(request):
    # body = json.loads(str(request.body))
    time.sleep(3)
    res = {"auc": str(random.random()), "f1": str(random.random()), "precision": str(random.random()), "recall": str(random.random()),
           "n_students": "123", "n_exercises": "1550", "total_num": "576681", "average_exercise": "25.321552",
           "model_name": "placeholder", "dataset": "placeholder"}
    return JsonResponse(res)


@api_view(['GET'])
def app_bar(request):
    file = open("./TestAPI/mock.json", "r")
    ret = json.load(file)
    return JsonResponse(ret)

@api_view(["POST"])
def inference_exercise(request):
    time.sleep(1)
    ret = { "pred_exercise": [ 0.12485866993665695, 0.04550475254654884, 0.011160857044160366, 0.0035634078085422516, 0.0016414602287113667, 0.0003102186892647296, 9.154443978331983e-05, 5.07793556607794e-05, 6.321274122456089e-05, 7.833219569874927e-05, 0.00011082676792284474, 8.401918603340164e-05, 0.00034297368256375194, 0.0005388534045778215, 0.0012303829425945878, 0.00465322146192193, 0.002241481328383088, 0.0011421921662986279, 0.0041079409420490265, 0.005799476522952318, 0.006846623960882425, 0.006067426409572363, 0.012919116765260696, 0.03835592046380043, 0.07588415592908859, 0.12214471399784088, 0.2209208756685257, 0.1758408397436142, 0.24416343867778778, 0.38924211263656616, 0.38054758310317993, 0.30875203013420105, 0.3706938922405243, 0.4231087267398834, 0.42336568236351013, 0.4606931209564209, 0.4796524941921234, 0.3975071609020233, 0.504805326461792, 0.5461576581001282, 0.453666627407074, 0.40373432636260986, 0.4128614068031311, 0.3789929747581482, 0.48351263999938965, 0.5369628667831421, 0.4487350285053253, 0.45895275473594666, 0.45149484276771545, 0.4087196886539459 ] }
    return JsonResponse(ret)

@api_view(["POST"])
def inference_step(request):
    time.sleep(1)
    res = { "pred_step": [ 0.6149722933769226, 0.4904051721096039, 0.9088562726974487, 0.48162680864334106, 0.9741768836975098, 0.8803252577781677, 0.5124295949935913, 0.5326528549194336, 0.8212955594062805, 0.9155654311180115, 0.9390671253204346, 0.5017739534378052, 0.15290774405002594, 0.6940552592277527, 0.5986979007720947, 0.13490669429302216, 0.7955902218818665, 0.735332727432251, 0.5716609358787537, 0.08212155848741531, 0.6239981651306152, 0.7901211977005005, 0.6014786958694458, 0.9052148461341858, 0.12485866993665695, 0.6424700021743774, 0.7704420685768127, 0.29706379771232605, 0.8404144048690796, 0.2514127790927887, 0.5802980661392212, 0.4938049912452698, 0.768913209438324, 0.49561020731925964, 0.9370214939117432, 0.8892242312431335, 0.6744257807731628, 0.8758289217948914, 0.8137779831886292, 0.920931875705719, 0.03904329240322113, 0.6897030472755432, 0.8760532736778259, 0.7339194416999817, 0.9672374725341797, 0.591905415058136, 0.07038300484418869, 0.04429059848189354, 0.9756441712379456, 0.9598090052604675, 0.9428064227104187 ] }
    return JsonResponse(res)

@api_view(["GET"])
def check_status(request):
    time.sleep(0.5)
    exp_status = 'notstarted'
    return JsonResponse({ 'status': exp_status })

@api_view(["GET"])
def start(request):
    return Response(status=status.HTTP_200_OK)

@api_view(["GET"])
def pred_tail(request):
    time.sleep(0.25)
    id = request.GET.get("id", None)
    return JsonResponse({'id': id})

class TestStructViewSet(ModelViewSet):
    def list(self, request):
        queryset = TestStruct.objects.all()
        serializer = TestStructSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = TestStructSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request):
        pass

    def retrieve(self, request):
        id = request.GET.get('id', None)
        result = TestStruct.objects.get(id=id)
        serializer = TestStructSerializer(result)
        return Response(serializer.data)
