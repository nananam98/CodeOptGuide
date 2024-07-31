
# Cấu Trúc Dữ Liệu và Giải Thuật

## 1. Giải Thuật
### 1.1 Định nghĩa
Giải thuật (algorithm) là một tập hợp hữu hạn các chỉ thị được xác định rõ ràng để giải quyết một vấn đề hoặc thực hiện một tác vụ cụ thể. Giải thuật thường được mô tả bằng ngôn ngữ tự nhiên, ngôn ngữ lập trình, hoặc dưới dạng sơ đồ hình học (flowchart).

### 1.2 Đọc giải thuật theo chuẩn hình học (diagram)
Một sơ đồ giải thuật (flowchart) là một biểu đồ thể hiện các bước thực hiện của giải thuật bằng các hình khối và mũi tên. Các hình khối thường gặp bao gồm:
- Hình chữ nhật: Thể hiện một bước xử lý hoặc hành động.
- Hình thoi: Thể hiện một bước kiểm tra điều kiện.
- Hình oval: Thể hiện điểm bắt đầu hoặc kết thúc của giải thuật.
- Mũi tên: Thể hiện luồng thực hiện của giải thuật.
- Hình bình hành: Thể hiện nhập hoặc xuất dữ liệu

## 2. Độ phức tạp của giải thuật
### 2.1 Định nghĩa
Độ phức tạp của giải thuật là một thước đo để đánh giá lượng tài nguyên (thời gian và không gian) cần thiết để thực hiện giải thuật.

### 2.2 Cách tính độ phức tạp của giải thuật
Độ phức tạp thời gian (time complexity) và độ phức tạp không gian (space complexity) thường được biểu diễn bằng ký hiệu Big-O, chẳng hạn O(1), O(n), O(log n), O(n^2).

### 2.3 Cách tối ưu giải thuật
Để tối ưu giải thuật, ta có thể:
- Giảm số lần lặp lại các bước.
- Sử dụng cấu trúc dữ liệu phù hợp.
- Tránh các thao tác không cần thiết.

## 3. Ví dụ cụ thể

### 3.1 Code dự án
```python
class GetPositionListByListID(APIView):  # lay locate theo danh sach id truyen vao

    @swagger_auto_schema(
        tags=["Locate"],
        request_body=swg.get_position_by_listid,
        operation_id='Get Position by list id',
        operation_description='Get Position by list id',
    )
    def post(self, request):
        try:
            if request.data['locate_type'] == 2:  # lay khu vuc cua tk
                list_zone = []
                list_id = request.data.get('list_id')
                locate = Locate.objects.filter(locate=2, account_id__in=list_id).values().distinct('custom_id')

                if request.data.get('distinct', None) == 0:  ### get zone no distinct
                    locate = Locate.objects.filter(locate=2, account_id__in=list_id).values()

                for l in locate:
                    obj = {'id': None, 'zone_name': None, 'account_id': l['account_id']}
                    zone = Zone.objects.filter(id=l['custom_id']).first()
                    if zone != None:
                        obj['id'] = zone.id
                        obj['zone_name'] = zone.zone_name
                    list_zone.append(obj)

                return Response(convert_response("Success", 200, list_zone))

            if request.data['locate_type'] == 1:  # lay vung cua tk

                list_area = []
                list_id = request.data.get('list_id')
                locate = Locate.objects.filter(locate=1, account_id__in=list_id).values().distinct('custom_id')

                if request.data.get('distinct', None) == 0:  ### get area no distinct
                    locate = Locate.objects.filter(locate=1, account_id__in=list_id).values()

                for l in locate:
                    obj = {"account_id": l['account_id'], 'id': None, "area_name": None}
                    area = Area.objects.filter(id=l['custom_id']).first()
                    if area != None:
                        obj['id'] = area.id
                        obj['area_name'] = area.area_name
                    list_area.append(obj)

                return Response(convert_response("Success", 200, list_area))

            if request.data['locate_type'] == 3:  # lay ca vung va khu vuc + vi tri
                dataReturn = []
                position_list = ['giám sát khu vực', 'trưởng vùng', 'nhân viên bán hàng', 'nhân viên thị trường']
                list_id = request.data.get('list_id')

                profile = RequestAPI.post("account/api/get_accounts_profile", json=
                {
                    "list_id": list_id
                }, service="account")
                profile = profile['data'] if profile['data'] and profile['status_code'] == 200 else []

                locate = Locate.objects.filter(account_id__in=list_id).values('custom_id', 'account_id', 'locate')
                for id in list_id:
                    obj = {'account_id': id, 'area': {}, 'zone': {}}
                    obj['profile'] = None
                    for prf in profile:
                        if prf['user_id'] == id and prf['profile'] != None:
                            for p in prf['profile']:
                                if p['value'].lower() in position_list:
                                    obj['profile'] = p['value']
                    for l in locate:
                        if l['account_id'] == id:
                            if l['locate'] == 1:
                                area = Area.objects.filter(id=l['custom_id']).first()
                                obj['area'] = {
                                    'area_name': area.area_name if area else None,
                                    'area_id': area.id if area else None,
                                }
                            if l['locate'] == 2:
                                zone = Zone.objects.filter(id=l['custom_id']).select_related('area').annotate(
                                    area_name=(F('area__area_name')), area_pk=(F('area__id'))).first()
                                obj['zone'] = {
                                    'zone_name': zone.zone_name if zone else None,
                                    'zone_id': zone.id if zone else None,
                                }
                                obj['area'] = {
                                    'area_name': zone.area_name if zone else None,
                                    'area_id': zone.area_pk if zone else None,
                                }
                        else:
                            continue
                    dataReturn.append(obj)

                return Response(convert_response("Success", 200, dataReturn))


        except Exception as error:
            return Response(str(error), 400)
```

![Sơ đồ giải thuật](https://raw.githubusercontent.com/nananam98/CodeOptGuide/main/data/flowchart_1.jpg)


### 3.2 Độ phức tạp của thuật toán
```python
if request.data['locate_type'] == 2:
    list_zone = []
    list_id = request.data.get('list_id')
    locate = Locate.objects.filter(locate=2, account_id__in=list_id).values().distinct('custom_id')

    if request.data.get('distinct', None) == 0:
        locate = Locate.objects.filter(locate=2, account_id__in=list_id).values()

    for l in locate:
        obj = {'id': None, 'zone_name': None, 'account_id': l['account_id']}
        zone = Zone.objects.filter(id=l['custom_id']).first()
        if zone != None:
            obj['id'] = zone.id
            obj['zone_name'] = zone.zone_name
        list_zone.append(obj)

    return Response(convert_response("Success", 200, list_zone))
```
Truy vấn cơ sở dữ liệu `Locate.objects.filter` có độ phức tạp `O(n)`, trong đó n là số lượng bản ghi trong `Locate`.  
Duyệt qua các bản ghi `locate` có độ phức tạp `O(m)`, trong đó m là số lượng bản ghi trả về từ truy vấn.  
Truy vấn cơ sở dữ liệu `Zone.objects.filter(id=l['custom_id']).first()` trong vòng lặp có độ phức tạp `O(1)` cho mỗi lần lặp, dẫn đến tổng độ phức tạp là `O(m)`.  
#### Tổng độ phức tạp cho khối này là `O(n) + O(m) + O(m) = O(n + 2m)`.

```python
if request.data['locate_type'] == 1:
    list_area = []
    list_id = request.data.get('list_id')
    locate = Locate.objects.filter(locate=1, account_id__in=list_id).values().distinct('custom_id')

    if request.data.get('distinct', None) == 0:
        locate = Locate.objects.filter(locate=1, account_id__in=list_id).values()

    for l in locate:
        obj = {"account_id": l['account_id'], 'id': None, "area_name": None}
        area = Area.objects.filter(id=l['custom_id']).first()
        if area != None:
            obj['id'] = area.id
            obj['area_name'] = area.area_name
        list_area.append(obj)

    return Response(convert_response("Success", 200, list_area))
```
Tương tự như khối trên, các truy vấn và vòng lặp có độ phức tạp tương tự.  
#### Tổng độ phức tạp cho khối này cũng là `O(n) + O(m) + O(m) = O(n + 2m)`.

```python
if request.data['locate_type'] == 3:
    dataReturn = []
    position_list = ['giám sát khu vực', 'trưởng vùng', 'nhân viên bán hàng', 'nhân viên thị trường']
    list_id = request.data.get('list_id')

    profile = RequestAPI.post("account/api/get_accounts_profile", json={
        "list_id": list_id
    }, service="account")
    profile = profile['data'] if profile['data'] and profile['status_code'] == 200 else []

    locate = Locate.objects.filter(account_id__in=list_id).values('custom_id', 'account_id', 'locate')
    for id in list_id:
        obj = {'account_id': id, 'area': {}, 'zone': {}}
        obj['profile'] = None
        for prf in profile:
            if prf['user_id'] == id and prf['profile'] != None:
                for p in prf['profile']:
                    if p['value'].lower() in position_list:
                        obj['profile'] = p['value']
        for l in locate:
            if l['account_id'] == id:
                if l['locate'] == 1:
                    area = Area.objects.filter(id=l['custom_id']).first()
                    obj['area'] = {
                        'area_name': area.area_name if area else None,
                        'area_id': area.id if area else None,
                    }
                if l['locate'] == 2:
                    zone = Zone.objects.filter(id=l['custom_id']).select_related('area').annotate(
                        area_name=(F('area__area_name')), area_pk=(F('area__id'))).first()
                    obj['zone'] = {
                        'zone_name': zone.zone_name if zone else None,
                        'zone_id': zone.id if zone else None,
                    }
                    obj['area'] = {
                        'area_name': zone.area_name if zone else None,
                        'area_id': zone.area_pk if zone else None,
                    }
            else:
                continue
        dataReturn.append(obj)

    return Response(convert_response("Success", 200, dataReturn))
```
Truy vấn API `RequestAPI.post` có độ phức tạp `O(p)` với p là số lượng profile trả về.  
Truy vấn cơ sở dữ liệu `Locate.objects.filter(account_id__in=list_id)` có độ phức tạp `O(n)`.  
Vòng lặp `for id in list_id` có độ phức tạp `O(k)` với k là số lượng ID trong `list_id`.  
Các vòng lặp bên trong có độ phức tạp tương ứng `O(p)` và `O(n)`.  
#### Tổng độ phức tạp cho khối này là `O(p) + O(n)` + `O(k * (p + n))`.

## 4. Giải pháp cải thiện
#### 4.1. Phương thức `post`.
```python
def post(self, request):
    try:
        locate_type = request.data.get('locate_type')
        list_id = request.data.get('list_id', [])
        distinct = request.data.get('distinct', None)

        if locate_type == 1:
            return self.get_areas(list_id, distinct)
        elif locate_type == 2:
            return self.get_zones(list_id, distinct)
        elif locate_type == 3:
            return self.get_full_details(list_id)
        else:
            return Response("Invalid locate_type", 400)

    except Exception as error:
        return Response(str(error), 400)
```

#### 4.1. Xử lý locate_type == 1 (Lấy vùng).
```python
def get_areas(self, list_id, distinct):
    list_area = []
    locate_query = Locate.objects.filter(locate=1, account_id__in=list_id).values()

    if distinct is not None and distinct == 0:
        locate_query = locate_query.distinct('custom_id')

    locate = locate_query
    custom_ids = [l['custom_id'] for l in locate]
    areas = {area.id: area for area in Area.objects.filter(id__in=custom_ids)}

    for l in locate:
        area = areas.get(l['custom_id'])
        obj = {
            'account_id': l['account_id'],
            'id': area.id if area else None,
            'area_name': area.area_name if area else None
        }
        list_area.append(obj)

    return Response(convert_response("Success", 200, list_area))
```
Truy vấn `Locate` một lần duy nhất và lấy danh sách `custom_id`.  
Truy vấn tất cả các `Area` với các `custom_id` đã lấy, lưu vào từ điển để truy xuất nhanh chóng.  
Độ phức tạp giảm xuống `O(n + m)`.

#### 4.2. Xử lý locate_type == 2 (Lấy khu vực).
```python
def get_zones(self, list_id, distinct):
    list_zone = []
    locate_query = Locate.objects.filter(locate=2, account_id__in=list_id).values()
    
    if distinct is not None and distinct == 0:
        locate_query = locate_query.distinct('custom_id')

    locate = locate_query
    custom_ids = [l['custom_id'] for l in locate]
    zones = {zone.id: zone for zone in Zone.objects.filter(id__in=custom_ids)}

    for l in locate:
        zone = zones.get(l['custom_id'])
        obj = {
            'id': zone.id if zone else None,
            'zone_name': zone.zone_name if zone else None,
            'account_id': l['account_id']
        }
        list_zone.append(obj)

    return Response(convert_response("Success", 200, list_zone))
```
Truy vấn `Locate` một lần duy nhất và lấy danh sách `custom_id`.  
Truy vấn tất cả các `Zone` với các `custom_id` đã lấy, lưu vào từ điển để truy xuất nhanh chóng.  
Độ phức tạp giảm xuống `O(n + m)`, trong đó n là số bản ghi `Locate` và m là số bản ghi `Zone`.

#### 4.3. Xử lý locate_type == 3 (Lấy cả vùng, khu vực và vị trí).
```python
def get_full_details(self, list_id):
    dataReturn = []
    position_list = ['giám sát khu vực', 'trưởng vùng', 'nhân viên bán hàng', 'nhân viên thị trường']

    profile_response = RequestAPI.post("account/api/get_accounts_profile", json={"list_id": list_id}, service="account")
    profiles = {prf['user_id']: prf for prf in profile_response.get('data', []) if prf['status_code'] == 200}

    locate = Locate.objects.filter(account_id__in=list_id).values('custom_id', 'account_id', 'locate')
    custom_ids = {l['custom_id'] for l in locate}
    
    areas = {area.id: area for area in Area.objects.filter(id__in=custom_ids)}
    zones = {zone.id: zone for zone in Zone.objects.filter(id__in=custom_ids).select_related('area').annotate(
        area_name=F('area__area_name'), area_pk=F('area__id'))}

    for id in list_id:
        obj = {
            'account_id': id,
            'area': {},
            'zone': {},
            'profile': None
        }
        
        profile = profiles.get(id)
        if profile and profile.get('profile'):
            obj['profile'] = next((p['value'] for p in profile['profile'] if p['value'].lower() in position_list), None)
        
        for l in locate:
            if l['account_id'] == id:
                if l['locate'] == 1:
                    area = areas.get(l['custom_id'])
                    obj['area'] = {
                        'area_name': area.area_name if area else None,
                        'area_id': area.id if area else None,
                    }
                elif l['locate'] == 2:
                    zone = zones.get(l['custom_id'])
                    obj['zone'] = {
                        'zone_name': zone.zone_name if zone else None,
                        'zone_id': zone.id if zone else None,
                    }
                    obj['area'] = {
                        'area_name': zone.area_name if zone else None,
                        'area_id': zone.area_pk if zone else None,
                    }
        
        dataReturn.append(obj)

    return Response(convert_response("Success", 200, dataReturn))
```
Truy vấn `Locate`, `Area` và `Zone` một lần và lưu trữ kết quả vào từ điển để truy xuất nhanh.  
Tối ưu hóa lấy thông tin `profile` bằng cách lưu trữ vào từ điển.  
Độ phức tạp giảm xuống `O(n + m + k)` trong đó n là số bản ghi `Locate`, m là số bản ghi `Area` và `Zone`, và k là số `profile`.  

#### Độ phức tạp tổng thể của mỗi khối xử lý đã được giảm xuống từ `O(p) + O(n)` + `O(k * (p + n))` còn `O(n + m)` hoặc `O(n + m + k)`.

![Biểu đồ tối ưu](https://raw.githubusercontent.com/nananam98/CodeOptGuide/main/data/chart_giai_thuat.png)