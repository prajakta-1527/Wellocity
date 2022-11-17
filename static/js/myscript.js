$(".plus-cart").click(function(){
    var id=$(this).attr("pid").toString();
    var elm=this.parentNode.children[2]
    var abc=$(this).parent().next().children(3).val()
    $.ajax({
        type: "GET",
        url: "pluscart",
        data: {
            prod_id : id
        },
        success : function(data){
            elm.innerText=data.quantity
            // abc.innerText=data.prodprice
            document.getElementById('amount').innerText=data.amount
            
        }
    })
})
$(".minus-cart").click(function(){
    var id=$(this).attr("pid").toString();
    var elm=this.parentNode.children[2]
    // var abc=this.parentNode.parentNode.children[2]
    var abc=$(this).parent().next().children(3).val().toString()
    console.log('working')
    console.log(abc)
    $.ajax({
        type: "GET",
        url: "minuscart",
        data: {
            prod_id : id
        },
        success : function(data){
            elm.innerText=data.quantity
            document.getElementById('amount').innerText=data.amount
            select.parent().next().children().next().next().val(data.prodprice);
        }
    })
})
$(".remove").click(function(){
    var id=$(this).attr("pid").toString();
    var elm=this
    $.ajax({
        type: "GET",
        url: "remove",
        data: {
            prod_id : id
        },
        success : function(data){
            
            document.getElementById('amount').innerText=data.amount
            elm.parentNode.parentNode.parentNode.parentNode.remove()


        }
    })
    
})
$(".removewish").click(function(){
    var id=$(this).attr("pid").toString();
    var elm=this
    $.ajax({
        type: "GET",
        url: "removewish",
        data: {
            prod_id : id
        },
        success : function(data){
            
            
            elm.parentNode.parentNode.remove()


        }
    })
    
})
$(".wishtocart").click(function(){
    var id=$(this).attr("pid").toString();
    var elm=this
    $.ajax({
        type: "GET",
        url: "wishtocart",
        data: {
            prod_id : id
        },
        success : function(data){
            elm.innerText=data.str


        }
    })
    
})
$.ajaxSetup({ headers: { 'csrftoken' : '{{ csrf_token() }}' } });
$(".addtowishlist").click(function(){
    var id=$(this).attr("pid").toString();
    var elm=this
    $.ajax({
        type: "GET",
        url: "/wishlist",
        data: {
            prod : id
        },
        success : function(data){
            
            document.getElementById('Abc').innerText=data.str
            console.log(data.str)

        }
    })
    
})