zero_pad = (x) ->
    if x < 10 then '0'+x else ''+x

Date::pretty_string = ->
    d = zero_pad(this.getDate())
    m = zero_pad(this.getMonth() + 1)
    y = this.getFullYear()
    y+'-'+m+'-'+ d

# loading
$.fn.spin = (opts) ->
  this.each () ->
    $this = $(this)
    data = $this.data()

    if data.spinner
      data.spinner.stop
      delete data.spinner

    if opts != false
      data.spinner = new Spinner $.extend(
          {
            color:$this.css 'color'
            lines: 11,
            length: 11,
            width: 5,
            radius: 10,
            corners: 1,
            rotate: 1.5,
            speed: 1.1,
            trail: 91,
          },
          opts
      )
      data.spinner.spin this
      data.spinner

# ajax add data by scroll
@NewDomain = class
  constructor: (@url, @starttime=null, @endtime=null) ->
    window.page = 0
    window.total = 0
    window.count = 0

  load_data: (loading, table_e, total_e, count_e) ->
    $.get @url, {'page':window.page, 'starttime':@starttime, 'endtime':@endtime}, (data) ->
      if data.domains
        window.page += 1
        total_e.html window.total = data.total
        for domain in data.domains
            window.count += 1
            table_e.append "<tr><td>"+window.count+"<\/td><td>"+domain+"<\/td><\/tr>"
      count_e.html window.count
      loading.hide()

# ajax add data by scroll
@IP = class
  constructor: (@url, @starttime=null, @endtime=null) ->
    window.page = 0
    window.total = 0
    window.count = 0

  load_data: (loading, table_e, total_e, count_e) ->
    $.get @url, {'page':window.page, 'starttime':@starttime, 'endtime':@endtime}, (data) ->
      if data.domains
        window.page += 1
        total_e.html window.total = data.total
        for domain in data.domains
            window.count += 1
            table_e.append "<tr><td>"+window.count+"<\/td><td>"+domain[0]+"<\/td><td>"+domain[1]+"<\/td><td>"+domain[2]+"<\/td><td>"+domain[3]+"<\/td><td>"+domain[4]+"<\/td><\/tr>"
      count_e.html window.count
      loading.hide()

@Domain = class
  constructor: (@url, @starttime=null, @endtime=null,@namelist=null,@typename=null) ->
    window.page = 0
    window.total = 0
    window.count = 0
    window.typename = @typename
  load_data: (loading, table_e, total_e, count_e) ->
    $.get @url, {'page':window.page, 'starttime':@starttime, 'endtime':@endtime,'namelist':@namelist}, (data) ->
      if data.domains
        window.page += 1
        total_e.html window.total = data.total
        for domain in data.domains
            window.count += 1
            if window.typename == 'namelistpercent'
              table_e.append "<tr><td>"+window.count+"<\/td><td>"+domain[0]+"<\/td><td>"+domain[1]+"<\/td><td>"+domain[2]+"<\/td><td>"+domain[3]+"<\/td><td>"+domain[4]+"<\/td><td>"+domain[5]+"<\/td><td>"+domain[6]+"<\/td><\/tr>"
            else 
              table_e.append "<tr><td>"+window.count+"<\/td><td>"+domain[0]+"<\/td><td>"+domain[1]+"<\/td><td>"+domain[2]+"<\/td><td>"+domain[3]+"<\/td><td>"+domain[4]+"<\/td><td>"+domain[5]+"<\/td><\/tr>"
      count_e.html window.count
      loading.hide()

# ajax add data by scroll
@Leadingin = class
  constructor: (@url, @starttime=null, @endtime=null) ->
    window.page = 0
    window.total = 0
    window.count = 0

  load_data: (loading, table_e, total_e, count_e) ->
    $.get @url, {'page':window.page, 'starttime':@starttime, 'endtime':@endtime}, (data) ->
      if data.domains
        window.page += 1
        total_e.html window.total = data.total
        for domain in data.domains
            window.count += 1
            table_e.append "<tr><td>"+window.count+"<\/td><td>"+domain[0]+"<\/td><td>"+domain[1]+"<\/td><td>"+domain[2]+"<\/td><td>"+domain[3]+"<\/td><\/tr>"
      count_e.html window.count
      loading.hide()
