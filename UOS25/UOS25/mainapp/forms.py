from django import forms
from mainapp.models import *
from bootstrap_datepicker_plus import DatePickerInput, DateTimePickerInput

#되나안되나모르겠다. html에 안들가지냐;
class ProductRegisterForm(forms.ModelForm):
    class meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'class':'form-control', 'placeholder' : field_name})
            self.fields[field_name].label = ''
#여기까지

class StoreRegisterForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'

    # Bootstrap CSS 적용
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'class':'form-control', 'placeholder' : field_name})
            self.fields[field_name].label = ''

class StoreUpdateForm(StoreRegisterForm):
    # PK 구분용
    id = forms.DecimalField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'id' : 'update_' + field_name})
    
        # 자동 PK
        # self.fields['id'].widget.attrs.update({'readonly' : True})

class StoreSearchForm(forms.Form):
    address = forms.CharField(max_length=80, required=False)
    contact = forms.CharField(max_length=20, required=False)
    store_pay_min = forms.DecimalField(min_value=0, required=False)
    store_pay_max = forms.DecimalField(max_value=1, required=False)

    # Bootstrap CSS 적용
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'class':'form-control', 'placeholder' : field_name})
            self.fields[field_name].label = ''

class SupplierRegisterForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

    # Bootstrap CSS 적용
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'class':'form-control', 'placeholder' : field_name})
            self.fields[field_name].label = ''

class SupplierUpdateForm(SupplierRegisterForm):
    # PK 구분용
    id = forms.DecimalField(widget=forms.HiddenInput())
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'id' : 'update_' + field_name})

        # 자동 PK
        # self.fields['id'].widget.attrs.update({'readonly' : True})

class SupplierSearchForm(forms.Form):
    name = forms.CharField(max_length=25, required=False)
    contact = forms.CharField(max_length=20, required=False)
    email = forms.CharField(max_length=40, required=False)

    # Bootstrap CSS 적용
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'class':'form-control', 'placeholder' : field_name})
            self.fields[field_name].label = ''

class CustomerRegisterForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

    # Bootstrap CSS 적용
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'class':'form-control', 'placeholder' : field_name})
            self.fields[field_name].label = ''

class CustomerUpdateForm(CustomerRegisterForm):
    # PK 구분용
    id = forms.DecimalField(widget=forms.HiddenInput())
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'id' : 'update_' + field_name})

        # 자동 PK
        # self.fields['id'].widget.attrs.update({'readonly' : True})

class CustomerSearchForm(forms.Form):
    name = forms.CharField(max_length=25, required=False)
    mileage_min = forms.DecimalField(min_value=0, required=False)
    mileage_max = forms.DecimalField(min_value=0, required=False)
    gender = forms.DecimalField(required=False)
    birthday_min = forms.DateField(required=False)
    birthday_max = forms.DateField(required=False)
    contact = forms.CharField(max_length=20, required=False)

    # Bootstrap CSS 적용
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'class':'form-control', 'placeholder' : field_name})
            self.fields[field_name].label = ''

class ProductRegisterForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    # Bootstrap CSS 적용
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'class':'form-control', 'placeholder' : field_name})
            self.fields[field_name].label = ''

class ProductUpdateForm(ProductRegisterForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'id' : 'update_' + field_name})

        # 바코드는 수정 불가
        self.fields['barcode'].widget.attrs.update({'readonly' : True})

class ProductSearchForm(forms.Form):
    barcode = forms.DecimalField(required=False)
    name = forms.CharField(max_length=50, required=False)
    supply_price_min = forms.DecimalField(min_value=0, required=False)
    supply_price_max = forms.DecimalField(min_value=0, required=False)
    unit_price_min = forms.DecimalField(min_value=0, required=False)
    unit_price_max = forms.DecimalField(min_value=0, required=False)
    supplier_id = forms.DecimalField(required=False)
    category_a = forms.DecimalField(required=False)
    category_b = forms.DecimalField(required=False)

    # Bootstrap CSS 적용
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'class':'form-control', 'placeholder' : field_name})
            self.fields[field_name].label = ''

class EmployeeRegisterForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['store_id']

        widgets = {'employed_date' : DatePickerInput(), 'fire_date' : DatePickerInput(), }

    # Bootstrap CSS 적용
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    #     for field_name in self.fields.keys():
    #         self.fields[field_name].widget.attrs.update({'class':'form-control', 'placeholder' : field_name})
    #         self.fields[field_name].label = ''
        self.fields['fire_date'].required = False

class EmployeeUpdateForm(EmployeeRegisterForm):
    # PK 구분용
    id = forms.DecimalField(widget=forms.HiddenInput())

    # 업데이트 폼 필드 자동 채우기 용
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'id' : 'update_' + field_name})

class FranchiseStoreRcptRegisterForm(forms.ModelForm):
    class Meta:
        model = Franchise_store_rcpt
        fields = '__all__'

    # Bootstrap CSS 적용
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'class':'form-control', 'placeholder' : field_name})
            self.fields[field_name].label = ''

class FranchiseStoreRcptUpdateForm(FranchiseStoreRcptRegisterForm):
    # PK 구분용
    id = forms.DecimalField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'id' : 'update_' + field_name})


class StockRegisterForm(forms.ModelForm):
    class Meta:
        model = Stock
        exclude = ['store_id']

    # Bootstrap CSS 적용
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'class':'form-control', 'placeholder' : field_name})
            self.fields[field_name].label = ''

class StockUpdateForm(StockRegisterForm):
    # PK 구분용
    id = forms.DecimalField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'id' : 'update_' + field_name})


class OrderRegisterForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_timestamp']

        widgets = {'order_timestamp' : DateTimePickerInput(), }

    # # Bootstrap CSS 적용
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name in self.fields.keys():
    #         self.fields[field_name].widget.attrs.update({'class':'form-control', 'placeholder' : field_name})
    #         self.fields[field_name].label = ''

class OrderListRegisterForm(forms.ModelForm):
    class Meta:
        model = Order_list
        fields = ['barcode', 'quantity']

    # # Bootstrap CSS 적용
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name in self.fields.keys():
    #         self.fields[field_name].widget.attrs.update({'class':'form-control', 'placeholder' : field_name})
    #         self.fields[field_name].label = ''

class StoreRefundRegisterForm(forms.ModelForm):
    class Meta:
        model = Store_refund
        fields = ['barcode', 'quantity', 'refund_timestamp', 'refund_reason_code']

        widgets = {'refund_timestamp' : DateTimePickerInput(), }

    # # Bootstrap CSS 적용
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name in self.fields.keys():
    #         self.fields[field_name].widget.attrs.update({'class':'form-control', 'placeholder' : field_name})
    #         self.fields[field_name].label = ''

class WorkListRegisterForm(forms.ModelForm):
    class Meta:
        model = Work_list
        fields = ['employee_id', 'workstart_timestamp', 'workend_timestamp']

        widgets = {'workstart_timestamp' : DateTimePickerInput(), \
            'workend_timestamp' : DateTimePickerInput() }

    # # Bootstrap CSS 적용
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name in self.fields.keys():
    #         self.fields[field_name].widget.attrs.update({'class':'form-control', 'placeholder' : field_name})
    #         self.fields[field_name].label = ''

class MaintenanceCostRegisterForm(forms.ModelForm):
    class Meta:
        model = Maintenance_cost
        exclude = ['store_id', 'storeowner_check']

        widgets = {'process_date' : DatePickerInput(), }

    # # Bootstrap CSS 적용
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name in self.fields.keys():
    #         self.fields[field_name].widget.attrs.update({'class':'form-control', 'placeholder' : field_name})
    #         self.fields[field_name].label = ''

class SalaryManageForm(forms.Form):
    date_min = forms.DateTimeField()
    date_max = forms.DateTimeField()

    # Bootstrap CSS 적용
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'class':'form-control', 'placeholder' : field_name})
            self.fields[field_name].label = ''
            
class ReceiptRegisterForm(forms.ModelForm):
    class Meta:
        model = Receipt
        exclude = ['store_id', 'trade_timestamp']

    # # Bootstrap CSS 적용
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    #     for field_name in self.fields.keys():
    #         self.fields[field_name].widget.attrs.update({'class':'form-control', 'placeholder' : field_name})
    #         self.fields[field_name].label = ''

        self.fields['customer_id'].required = False
        self.fields['employee_id'].empty_label = "점원 선택"
        self.fields['customer_id'].empty_label = "손님 선택"

class TradeListRegisterForm(forms.ModelForm):
    class Meta:
        model = Trade_list
        fields = ['barcode', 'quantity']

    # # Bootstrap CSS 적용
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    #     for field_name in self.fields.keys():
    #         self.fields[field_name].widget.attrs.update({'class':'form-control', 'placeholder' : field_name})
    #         self.fields[field_name].label = ''
        
        self.fields['barcode'].empty_label = "상품 선택"