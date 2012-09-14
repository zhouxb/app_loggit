zero_pad = (x) ->
    if x < 10 then '0'+x else ''+x

Date::pretty_string = ->
    d = zero_pad(this.getDate())
    m = zero_pad(this.getMonth() + 1)
    y = this.getFullYear()
    y + m + d

now = new Date
console.log now.pretty_string()

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

