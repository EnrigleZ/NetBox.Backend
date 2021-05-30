# Create your views here.
from MTS.serializer import serialize_TDMTree_index
from MTS.models import TDMNode, TDMTree
from configs import MEDIA_ROOT
import os
from django.http import JsonResponse, HttpResponse
from pathlib import Path
import numpy as np
from datetime import datetime

mts_path = os.path.join(MEDIA_ROOT, 'mts')
Path(mts_path).mkdir(exist_ok=True)

def join(*args):
    return os.path.join(mts_path, *args)

TDMTree.load(join('temp.tree'))

def genereteTree(request):
    children_limits = request.POST['limits']
    children_limits = [int(x) for x in children_limits.split(',')]
    if children_limits[-1] != 0:
        children_limits.append(0)
    timestamp = datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
    tree = TDMTree.generateRandom(len(children_limits), children_limits)
    tree.dump(join(timestamp))
    return JsonResponse({
        'name': timestamp,
    }, safe=False)

def getTrees(request):
    names = os.listdir(mts_path)
    return JsonResponse(names, safe=False)

def getTree(request):
    name = request.GET['name']
    sample_children = int(request.GET['children'])
    sample_depth = int(request.GET['depth'])
    if not Path(join(name)).exists():
        return JsonResponse({
            'msg': 'Tree file not exists',
            'name': name,
        }, status=404)

    tree = TDMTree.load(join(name))
    return JsonResponse(serialize_TDMTree_index(tree, sample_children, sample_depth), safe=False)
